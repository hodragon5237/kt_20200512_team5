# 사용자로부터 숫자를 N, M을 입력받아 N과 M의 최대공약수와 최소공배수를 출력하세요. 
# /commons?num=N

from flask import Flask, request
import math

app=Flask(__name__)
app.env="development"
app.debug=True

def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def lcm(x,y):
    return x*y//gcd(x,y)

@app.route('/commons')
def commons():
    N=request.args.get('num')
    if "," not in N:
        return "오입력(변수 2개 필요)입니다. 다시 입력해주세요.(호출예시 : /commons?num=x,y)"

    N=N.split(',')
    if not N[0].isnumeric():
        return "not number"
    elif not N[1].isnumeric():
        return "not number"

    x=int(N[0])
    y=int(N[1])

    if int(x) <= 0:
        return "wrong number"
    elif int(y) <= 0:
        return "wrong number"
    
    result = "요청하신 작업에 대한 답변 드립니다.<br> {0}와 {1}의 최대공약수는 {2}, 최소공배수는 {3}"
    gcd_result=gcd(x,y)
    lcm_result=lcm(x,y)

    return result.format(x,y,gcd_result,lcm_result)

app.run()