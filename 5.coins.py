# 사용자로부터 숫자를 N을 입력받아, 1, 5, 10, 25, 50의 숫자를 이용하여 최소 갯수로 N을 표현해보자 
# 예) 183 = 50 * 3 + 25 * 1 + 5 * 1 + 1 * 3 => 총 8개
# /coins?num=N


from flask import Flask, request
import math

app=Flask(__name__)
app.env="development"
app.debug=True

@app.route('/coins')
def coins():
    EA=0
    coin_dict={}
    coins=[50,25,10,5,1]
    N=request.args.get('num')

    if not N.isnumeric():
        return "문자 또는 음수를 호출하셨습니다. 다시 입력해주세요."

    elif int(N) <= 0:
        return "0을 호출하셨습니다. 다시 입력해주세요."

    for n in coins:
        R = int(N) // n
        coin_dict[str(n)] = R
        EA += R
        N = int(N)-n*R 
        
    return "요청하신 수에 대한 환전 세부내용은 {0}입니다.<br> 총 코인수(최소갯수)는 {1}입니다.".format(str(coin_dict), str(EA))

app.run()