# 사용자로부터 2 ~ 9 사이의 숫자를 입력 받은 후, 해당 숫자에 대한 구구단을 출력하세요.
# /gugu/<number>

from flask import Flask, request

app=Flask(__name__)
app.env="development"
app.debug=True

@app.route('/gugu/<number>')
def gugu(number):
    result_list=["※ 주의사항 : 2 ~ 9 사이의 숫자만 호출 가능합니다. ","##### 구구단 {0}단 #####".format(number)]
    if not number.isnumeric():
        return "not number"
    elif int(number) not in range(2,10):
        return "wrong number"
    for i in range(1,10):
        result=int(number)*i
        result_list.append(number+"X"+str(i)+"="+str(result))
    
    return '<br>'.join(result_list)

app.run()