import jwt
from .base import JwtABC,JwtCustomAttr

class JwtBuilder(JwtABC):

    def __init__(self,payload:dict):
        self.payload=payload
        self.attr=JwtCustomAttr(payload=self.payload,access_token_exp=13,refresh_token_exp=17)
    
    
    def get_token(self)->dict:
        tokens={
            "access_token":jwt.encode(payload=self.attr.access_token_dict,key=self.attr.jwt_secret,algorithm=self.attr.jwt_algos),
            "refresh_token":jwt.encode(payload=self.attr.refresh_token_dict,key=self.attr.jwt_secret,algorithm=self.attr.jwt_algos),
        }
        return tokens

    

