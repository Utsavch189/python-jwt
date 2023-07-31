from jwt_v2.token import JwtBuilder
from time import sleep

a=JwtBuilder(payload={
    "sub":"utsav"
})
#print("a: ",a.get_token())
#sleep(120)
b=JwtBuilder(payload={
    "sub":"supu"
})
#print("b: ",b.get_token())

res=JwtBuilder(token="eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2OTA3ODA0MDEuMzQ5MTk5LCJleHAiOjE2OTA3ODExODEuMzQ5MTk5LCJzdWIiOiJzdXB1In0.P9tx3S8bVPvplA8AMPDikbRS2a5eGFWXHR1XsFudWc5q5yVKBMpkAlUBzUnozl0Ihe6Ac0RlWSFesr8ZsBj4kw")
print(res.decode())