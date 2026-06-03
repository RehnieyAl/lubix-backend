
from pydantic import BaseModel, EmailStr, field_validator
from app.models.ModelEventToken import TokenType
import re


class CreateCompany(BaseModel):
    companyName: str
    email: EmailStr
    password: str
    nit: str
    tell: str
    address: str
    isActive: bool = True
    verified: bool = False

    @field_validator('companyName')
    def validate_company_name(cls, v: str):
        if len(v) < 3:
            raise ValueError('el nombre de la empresa debe tener al menos 3 caracteres')
        if len(v) > 80:
            raise ValueError('el nombre de la empresa no debe exceder los 80 caracteres')
        return v

    @field_validator('email')
    def validate_email(cls, v: str):
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', v):
            raise ValueError('correo electrónico no válido')
        return v

    @field_validator('password')
    def validate_password(cls, v: str):
        if len(v) < 8:
            raise ValueError('la contraseña debe tener al menos 8 caracteres')
        if not re.search(r'[A-Z]', v):
            raise ValueError('la contraseña debe contener al menos una letra mayúscula')
        if not re.search(r'[a-z]', v):
            raise ValueError('la contraseña debe contener al menos una letra minúscula')
        if not re.search(r'[0-9]', v):
            raise ValueError('la contraseña debe contener al menos un número')
        return v

    @field_validator('tell')
    def validate_tell(cls, v: str):
        if len(v) < 10:
            raise ValueError('el número de teléfono debe tener al menos 10 caracteres')
        return v

    @field_validator('nit')
    def validate_nit(cls, v: str):
        if len(v) < 5:
            raise ValueError('el NIT no es válido')
        return v

    @field_validator('address')
    def validate_address(cls, v: str):
        if len(v) < 5:
            raise ValueError('la dirección debe tener al menos 5 caracteres')
        return v


class VerifyCompanyEmail(BaseModel):
    email: EmailStr
    code: str

    @field_validator('code')
    def validate_code(cls, v: str):
        if len(v) != 6:
            raise ValueError('el código debe tener exactamente 6 caracteres')
        if not v.isdigit():
            raise ValueError('el código debe contener solo números')
        return v


class CompanyLogin(BaseModel):
    email: EmailStr
    password: str


class ForgotCompanyPassword(BaseModel):
    email: EmailStr


class ResetCompanyPassword(BaseModel):
    email: EmailStr
    code: str
    new_password: str

    @field_validator('code')
    def validate_code(cls, v: str):
        if len(v) != 6:
            raise ValueError('el código debe tener exactamente 6 caracteres')
        if not v.isdigit():
            raise ValueError('el código debe contener solo números')
        return v

    @field_validator('new_password')
    def validate_new_password(cls, v: str):
        if len(v) < 8:
            raise ValueError('la contraseña debe tener al menos 8 caracteres')
        if not re.search(r'[A-Z]', v):
            raise ValueError('la contraseña debe contener al menos una letra mayúscula')
        if not re.search(r'[a-z]', v):
            raise ValueError('la contraseña debe contener al menos una letra minúscula')
        if not re.search(r'[0-9]', v):
            raise ValueError('la contraseña debe contener al menos un número')
        return v


class AddCompanyToken(BaseModel):
    id: int
    token: TokenType = TokenType.access


class DeleteCompanyToken(BaseModel):
    id: int
    token: TokenType = TokenType.access





