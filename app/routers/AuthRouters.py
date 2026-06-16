# Este router se encarga de manejar las rutas relacionadas 
# con la autenticación de usuarios, incluyendo registro, inicio de sesión,
# verificación de correo electrónico, recuperación de contraseña y cierre de sesión.
from fastapi import APIRouter,Depends, UploadFile, File, Form
from app.services.authentication.AuthService import register_user_service,register_company_service,verify_email_service, login_user_service,login_company_service, forgot_password_service, reset_password_service
from sqlalchemy.orm import Session
from app.database.Connection import get_db
from app.schemas.SchemaAuthUser import createUser, verifyEmail, userLogin, forgotPassword, ResetPassword
from app.schemas.SchemaAuthCompany import createCompany, LoginCompany
from app.services.NasService import subir


router = APIRouter(
    prefix=("/Auth"),   
    tags=["Auth"]
)

@router.post("/register-user")
def registerUser(user: createUser, database: Session = Depends(get_db)):
    register_user_service(user, database)
    return {
        "message": "Usuario registrado correctamente, se ha enviado un código de verificación a tu correo electrónico para verificar tu cuenta.",
    }

@router.post("/register-company")
def registerCompany(
    fullName: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    tell: str = Form(...),
    companyName: str = Form(...),
    companyAddress: str = Form(...),
    companyNIT: str = Form(...),
    companyNITDV: str = Form(...),
    certificate: UploadFile = File(...),
    database: Session = Depends(get_db)):

    user = createUser(
        fullName=fullName,
        email=email,
        password=password,
        tell=tell
    )

    company = createCompany(
        companyName=companyName,
        companyAddress=companyAddress,
        companyNIT=companyNIT,
        companyNITDV=companyNITDV
    )
    path = "companies/{company_nit}/certificates/"
    certificate_result = subir.upload_file(certificate, path)
    
    return register_company_service(user,company, certificate_result, database)

@router.post("/verify-email-user")
def verify_email(code: verifyEmail, database: Session = Depends(get_db)):
    result = verify_email_service(code, database)
    return result

@router.post("/login-user")
def login_user(user: userLogin, database: Session = Depends(get_db)):
    result = login_user_service(user, database)
    return result

@router.post("/login-company")
def login_company(company: LoginCompany, database: Session = Depends(get_db)):
    result = login_company_service(company, database)
    return result

@router.post("/forgot-password-user")
def forgot_password(user: forgotPassword, database: Session = Depends(get_db)):
    result = forgot_password_service(user, database)
    return result

@router.post("/reset-password-user")
def reset_password(user: ResetPassword, database: Session = Depends(get_db)):
    result = reset_password_service(user, database)
    return result
