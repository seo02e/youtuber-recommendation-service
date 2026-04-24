from pydantic import BaseModel

class SignupRequest(BaseModel):
    user_id: str
    user_password:str
    user_name:str
    
class SignupResponse(BaseModel):
    message : str
    user_name : str
    
class LoginRequest(BaseModel):
    user_id:str
    user_password:str
    
class LoginResponse(BaseModel):
    message : str
    user_name :str
    