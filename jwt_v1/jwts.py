import jwt
from datetime import datetime,timedelta


jwt_secret='utsavsupratim'
jwt_algos='HS512'

class JWT_Builder:
    def __init__(self,payload,enc=None):
        self.payload=payload
        self.enc=enc
        self.now = datetime.now()
        self.key=jwt_secret
        self.algo=jwt_algos

    def concat(self,a):
        return {**a,**self.payload}

    def get_token(self):
        access_token_exp=datetime.timestamp(self.now+timedelta(minutes=11))
        refresh_token_exp=datetime.timestamp(self.now+timedelta(minutes=14))

        access_token=jwt.encode(self.concat(a={"exp":access_token_exp,"iat":(datetime.timestamp(self.now))}),self.key,algorithm=self.algo)
        resfresh_token=jwt.encode(self.concat(a={"exp":refresh_token_exp,"iat":(datetime.timestamp(self.now))}),self.key,algorithm=self.algo)
        data={
            "access_token":access_token,
            "refresh_token":resfresh_token
        }
        return data
    