
# 사용자로부터 숫자를 N을 입력받은 후 1부터 N까지의 숫자 중 소수만 출력하세요.
# /prime?num=N

from flask import Flask, request
import math

app=Flask(__name__)
app.env="development"
app.debug=True

@app.route('/prime')
def prime():
    N=request.args.get('num')
    primes =["요청하신 수 1부터 {0}까지의 숫자 중 소수는 다음과 같습니다.<br>".format(N)]

    if not N.isnumeric():
        return "문자 또는 음수를 호출하셨습니다. 다시 입력해주세요."

    elif int(N) <= 1:
        return "0 또는 1을 호출하셨습니다. 다시 입력해주세요."

    # try:
    #     N = int(N)
    # except:
    #     return "not number"
        
    for i in range(2, int(N)+1):
        common_count = 0
        for n in range(1,int(i)+1):
            if i % n == 0 :
                common_count += 1
        if common_count == 2:
            primes.append(str(i))
    primes.append("")

    return "/".join(primes)

app.run()