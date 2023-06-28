from abc import ABC,abstractmethod
from dataclasses import dataclass,field
from datetime import datetime,timedelta

def access_token():
    a={"iat":datetime.timestamp(datetime.now())}
    b={"exp":datetime.timestamp(datetime.now()+timedelta(minutes=11))}
    return {**a,**b}

def refresh_token():
    a={"iat":datetime.timestamp(datetime.now())}
    b={"exp":datetime.timestamp(datetime.now()+timedelta(minutes=14))}
    return {**a,**b}

class JwtABC:
    @abstractmethod
    def get_token(self)->dict:pass


@dataclass(init=False)
class JwtOwnAttr:
    jwt_secret:str='utsavsupratim'
    jwt_algos:str='HS512'
    access_token_exp_iat:dict=field(default_factory=access_token)
    refresh_token_exp_iat:dict=field(default_factory=refresh_token)

@dataclass
class JwtCustomAttr(JwtOwnAttr):
    payload:dict=field(default_factory=dict)
    access_token_dict:dict=field(default_factory=dict,init=False)
    refresh_token_dict:dict=field(default_factory=dict,init=False)

    def __post_init__(self):
        self.access_token_dict={**self.access_token_exp_iat,**self.payload}
        self.refresh_token_dict={**self.refresh_token_exp_iat,**self.payload}
