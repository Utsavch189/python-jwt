from jwt_v2.token import JwtBuilder
from time import sleep

a=JwtBuilder(payload={
    "name":"utsav"
})
print("a: ",a.get_token())
sleep(120)
b=JwtBuilder(payload={
    "name":"supu"
})
print("b: ",b.get_token())
