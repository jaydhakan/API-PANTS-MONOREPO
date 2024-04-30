from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from apps.auth.src.dto import UserLoginReqBody
from apps.auth.src.service import auth_service
from libs.utils.jwt.src.helpers import jwt_helpers

auth_route = APIRouter(tags=['Authentication'])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


@auth_route.get('/{path:path}', include_in_schema=False)
def default_route():
    return {'message': 'Server is up and running 🚀🚀🚀'}


@auth_route.post("/token")  # separate route for FastAPI swagger login
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth_service.generate_token_for_swagger(form_data)


@auth_route.post('/auth/login')
def auth_login(request_data: UserLoginReqBody):
    try:
        access_token = auth_service.generate_token(request_data)
        return JSONResponse(
            {'message': 'Login Successful', 'access_token': access_token}, 200
        )
    except Exception as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error message: {str(e)}'
        )


@auth_route.post('/auth/logout')
def auth_logout(access_token: str = Depends(jwt_helpers.is_token_valid)):
    try:
        auth_service.remove_token(access_token)
        return {'message': 'Logout successful'}, 200
    except Exception as e:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error message: {str(e)}'
        )
