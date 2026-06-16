# Este servicio se encarga de manejar la lógica de autenticación de usuarios, 
# incluyendo registro, inicio de sesión, verificación de correo electrónico, 
# recuperación de contraseña y cierre de sesión.
from fastapi import HTTPException
from datetime import datetime, timedelta
from app.models.ModelCompany import Company
from app.models.ModelRefreshToken import refreshToken
from app.models.ModelUser import Users
from app.models.ModelRole import Role
from app.schemas.SchemaAuthUser import (
    createUser, 
    verifyEmail, 
    userLogin, 
    forgotPassword, 
    ResetPassword
)
from .JWTService import create_access_token, create_refresh_token
from app.schemas.SchemaAuthCompany import createCompany, LoginCompany
from sqlalchemy.orm import Session
from app.utils.Security import hash_password, verify_password
from app.services.email.SaveAndGenerateCode import create_code_and_send_code, verify_code
from app.services.email.template.EmailRegisterCompany import EmailRegisterCompany

def register_user_service(user: createUser, database: Session):
    user_role = database.query(Role).filter(Role.name == "USER").first()
    exists_user = database.query(Users).filter(Users.email == user.email).first()
    if exists_user:
        raise HTTPException(status_code=409, detail="correo en uso")
    
    try:

        hashed_password = hash_password(user.password)
        new_user = Users(
            fullName = user.fullName,
            email = user.email,
            hashed_password = hashed_password,
            role_id = user_role.id,
            tell = user.tell,
            isActive = user.isActive,
            verified = user.verified,
        )
    
        database.add(new_user)
        database.commit()
        database.refresh(new_user)
        confirm_id_user = database.query(Users).filter(Users.email == user.email).first()
        create_code_and_send_code(database, confirm_id_user.id, email=user.email, code_type="verifyEmail")
        return {
            "message": "Usuario registrado correctamente, se ha enviado un código de verificación a tu correo electrónico para verificar tu cuenta."
        }
    
    except Exception as e:
        database.rollback()

        print("ERROR:",e)
        raise HTTPException(status_code=500, detail="Error al crear cuenta")

def register_company_service(user: createUser, company: createCompany, certificate_result: str, database: Session):
    company_role = database.query(Role).filter(Role.name == "company").first()
    exists_NIT = database.query(Company).filter(Company.CompanyNIT == company.companyNIT).first()
    exists_email = database.query(Users).filter(Users.email == user.email).first()

    if not company_role:
        raise HTTPException(status_code=409, detail="Ups no hay rol para empresa")
    
    if exists_NIT:
        raise HTTPException(status_code=409, detail="NIT en uso")
    
    if exists_email:
        raise HTTPException(status_code=409, detail="Correo en uso")
    

    try:
        hashed_password = hash_password(user.password)
        new_user = Users(
            fullName = user.fullName,
            email = user.email,
            hashed_password = hashed_password,
            role_id = company_role.id,
            tell = user.tell,
            isActive = user.isActive,
            verified = user.verified,
        )

        database.add(new_user)
        database.flush()

        new_company = Company(
            user_id = new_user.id,
            nameCompany = company.companyName,
            addressCompany = company.companyAddress,
            CompanyNIT = company.companyNIT,
            CompanyNITDV = company.companyNITDV,
            CompanyLogo = company.companyLogo,
            CompanyBanner = company.companyBanner,
            CompanyCertificate = certificate_result["path"],
        )

        database.add(new_company)
        database.commit()
        database.refresh(new_company)
        EmailRegisterCompany(user.email, company.companyName, company.companyNIT)

        return {
            "message": "Empresa registrada correctamente. espera que el equipo de Lubix se ponga en contacto contigo para verificar tu empresa y activar tu cuenta.",
            "certificate_url": new_company.CompanyCertificate,
            "company_name": new_company.nameCompany,
            "company_nit": new_company.CompanyNIT,
            "certificate": certificate_result["path"]
        }
    
    except Exception as e:
        database.rollback()
        print("ERROR",e)

        raise HTTPException(status_code=500, detail="Error al crear cuenta empresarial")

def verify_email_service(code: verifyEmail, database: Session):
    user = database.query(Users).filter(Users.email == code.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="Correo incorrecto")
    
    if not verify_code(database, user.id, code.code, code_type="verifyEmail"):
        code = create_code_and_send_code(database, user.id, user.email, code_type="verifyEmail")
        return {
            "message": "Código de verificación incorrecto o expirado. Se ha enviado un nuevo código a tu correo electrónico.",
            "code": code
        }
    
    user.verified = True
    database.commit()

    return {
        "verified": user.verified,
        "message": "Correo electrónico verificado correctamente"
    }

def login_user_service(user: userLogin, database: Session):
    search_user = database.query(Users).filter(Users.email == user.email).first()
    if not search_user:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    
    if not verify_password(user.password, search_user.hashed_password):
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    
    if not search_user.verified:
        create_code_and_send_code(database, search_user.id, search_user.email, code_type="verifyEmail")
        return {
            "message": "Tu correo electrónico no ha sido verificado. Se ha enviado un nuevo código de verificación a tu correo electrónico."
        }
        
    access_token = create_access_token(
        str(search_user.id),
        str(search_user.role_id)
    )


    refresh_token = create_refresh_token(
        str(search_user.id)
    )
    
    db_refresh = refreshToken(
        token=refresh_token,
        user_id=search_user.id,
        revoked=False,
        expires_at=datetime.utcnow() + timedelta(days=15)
    )

    database.add(db_refresh)
    database.commit()

    return {
        "message": "Inicio de sesión exitoso",
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "id": search_user.id,
        "Nombre": search_user.fullName,
        "email": search_user.email,
        "role": search_user.role_id
    }

def login_company_service(company: LoginCompany, database: Session):
    search_company = database.query(Users).join(Company, Users.id == Company.user_id).filter(Company.CompanyNIT == company.companyNIT).first()
    
    if not search_company:
        raise HTTPException(status_code=400, detail="NIT o contraseña incorrectos")
    
    if not verify_password(company.companyPassword, search_company.hashed_password):
        raise HTTPException(status_code=400, detail="NIT o contraseña incorrectos")
    
    access_token = create_access_token(
        user_id=str(search_company.id),
        role=search_company.role.name
    )

    refresh_token = create_refresh_token(
        user_id=str(search_company.id)
    )

    db_refresh = refreshToken(
        token=refresh_token,
        user_id=search_company.id,
        revoked=False,
        expires_at=datetime.utcnow() + timedelta(days=15)
    )
    
    database.add(db_refresh)
    database.commit()

    return {
        "message": "Inicio de sesión exitoso",
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "id": search_company.id,
        "email": search_company.email,
        "role": search_company.role_id
    }

def forgot_password_service(user: forgotPassword, database: Session):
    search_user = database.query(Users).filter(Users.email == user.email).first()
    if not search_user:
        raise HTTPException(status_code=400, detail="Correo no registrado")
    create_code_and_send_code(database, search_user.id, user.email, code_type="resetPassword")
    return {
        "message": "se ha enviado un código de recuperación de contraseña a tu correo electrónico."
    }

def reset_password_service(user: ResetPassword, database: Session):
    search_user = database.query(Users).filter(Users.email == user.email).first()
    if not search_user:
        raise HTTPException(status_code=400, detail="Correo no registrado")
    
    if not verify_code(database, search_user.id, user.code, code_type="resetPassword"):
        raise HTTPException(status_code=400, detail="Código de recuperación de contraseña incorrecto o expirado.")
    
    hashed_password = hash_password(user.new_password)
    search_user.hashed_password = hashed_password
    database.commit()
    
    return {
        "message": "Contraseña restablecida correctamente"
    }
