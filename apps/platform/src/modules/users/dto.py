from pydantic import BaseModel, EmailStr, Field

from libs.utils.common.src.modules.enums import Role


class RegisterUserReqBody(BaseModel):
    firstName: str = Field(
        description='Your First Name',
        example='Jay',
        min_length=1,
        max_length=20
    )
    lastName: str = Field(
        description='Your Last Name',
        example='Dhakan',
        min_length=1,
        max_length=20
    )
    userId: str = Field(
        description="User's id.",
        example='jay1234',
        min_length=1,
        max_length=20
    )
    email: EmailStr = Field(
        description='Your email address',
        example='jay@gmail.com',
        min_length=4,
        max_length=20
    )
    password: str = Field(
        description='Your password',
        example='jay1234',
        min_length=1,
        max_length=20
    )
    privilege: str = Field(
        description='Specify your role',
        example=Role.SUPER_ADMIN.value
    )


class UpdateUserReqBody(BaseModel):
    firstName: str = Field(
        description='Your First Name',
        example='Jay',
        min_length=1,
        max_length=20,
        default=None
    )
    lastName: str = Field(
        description='Your Last Name',
        example='Dhakan',
        min_length=1,
        max_length=20,
        default=None
    )
    password: str = Field(
        description='Your password',
        example='xyz1234',
        min_length=1,
        max_length=20,
        default=None
    )
