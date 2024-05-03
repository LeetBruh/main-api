from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse, Response

from auth.auth_handler import sign_jwt
from models import UserCred, User
from models.db_session import get_session
from pydantic_models.user import UserLoginOut, UserLoginIn, UserRegisterIn, UserRegisterOut
from utils.password import hash_password

EXPIRE_TIME: int = 60 * 60 * 24 * 30

router: APIRouter = APIRouter()


@router.post(
    path="/register",
    summary="Register",
    operation_id="register",
    description="Register new user",
    response_model=UserRegisterOut
)
async def register_user(
    register: UserRegisterIn,
    session: AsyncSession = Depends(get_session)
) -> dict[str, str] | Response:
    user = User(first_name=register.first_name, last_name=register.last_name)
    session.add(user)
    try:
        user_cred = UserCred(login=register.login, password=hash_password(register.password), role=register.role)
        await user_cred.save(session)
    except IntegrityError:
        return JSONResponse(status_code=403, content={"description": "User already exists"})
    user_cred.user_id = user.id
    await session.commit()
    return {"token": sign_jwt("user_id", user.id, register.role, EXPIRE_TIME)}


@router.post(
    path="/login",
    summary="Login",
    operation_id="login",
    description="Login as user",
    response_model=UserLoginOut
)
async def login_user(
    login: UserLoginIn,
    session: AsyncSession = Depends(get_session)
) -> dict[str, str] | Response:
    user_cred = await UserCred.get_by_login(login.login, session)
    if user_cred and user_cred.password == hash_password(login.password):
        return {"token": sign_jwt("user_id", user_cred.user_id, user_cred.role, EXPIRE_TIME)}
    return Response(status_code=403)
