from fastapi import APIRouter, HTTPException
from app.shemas import auth_schema

router = APIRouter(tags=["auth"])

@router.post("/signup", response_model=auth_schema.SignupResponse, )
def new_user(request: auth_schema.SignupRequest):
    return auth_schema.SignupResponse(
        message="회원가입에 성공하였습니다.",
        user_name=request.user_name
    )


@router.post("/login", response_model=auth_schema.SignupResponse)
def login(regquest: auth_schema.LoginRequest):
    if not regquest.user_id or not regquest.user_password:
        raise HTTPException(status_code=400,detail= "데이터가 존재하지 않습니다.")
    return auth_schema.LoginResponse(
        message="로그인에 성공하였습니다.",
        user_name= regquest.user_name
    )