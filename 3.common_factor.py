# 사용자로부터 숫자를 N을 입력받아. N의 약수를 모두 출력하세요. 
# /common_factor?num=N

from flask import Flask, request
import math

app=Flask(__name__)
app.env="development"
app.debug=True


@app.route('/common_factor')
def common_factor():
    N=request.args.get('num')
    common_factors =["요청하신 수 {0}의 약수는 다음과 같습니다.<br>".format(N)]

    if not N.isnumeric():
        return "문자 또는 음수를 호출하셨습니다. 다시 입력해주세요."

    elif int(N) <= 1:
        return "0 또는 1을 호출하셨습니다. 다시 입력해주세요."

    for n in range(1,int(N)+1):
        if int(N) % n == 0 :
            common_factors.append(str(n))
            
    common_factors.append("")

    return "/".join(common_factors)

app.run()