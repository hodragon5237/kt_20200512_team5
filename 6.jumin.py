# 주민등록번호를 입력받아 올바른 주민번호인지 검증하라.
# 주민번호 : ① ② ③ ④ ⑤ ⑥ - ⑦ ⑧ ⑨ ⑩ ⑪ ⑫ ⑬
# 합계 
# = 마지막수를 제외한 12자리의 숫자에 2,3,4,5,6,7,8,9,2,3,4,5 를 순서대로 곱산수의 합
# = ①×2 + ②×3 + ③×4 + ④×5 + ⑤×6 + ⑥×7 + ⑦×8 + ⑧×9 + ⑨×2 + ⑩×3 + ⑪×4 + ⑫×5
# 나머지 = 합계를 11로 나눈 나머지
# 검증코드 = 11 - 나머지
# 여기서 검증코드가 ⑬자리에 들어 갑니다.
#
# /jumin 
# with form post

# def verify_jumin(serial):
#     return False

# verify_jumin('101010-2020200')

from flask import Flask, request
import math

app=Flask(__name__,static_folder='static')
app.env="development"
app.debug=True

def get_template(filename):
    with open(f'./{filename}', 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def verify_jumin(serial):
    sum_0=int(serial[0])*2+int(serial[1])*3+int(serial[2])*4+int(serial[3])*5+int(serial[4])*6+int(serial[5])*7+int(serial[7])*8+int(serial[8])*9+int(serial[9])*2+int(serial[10])*3+int(serial[11])*4+int(serial[12])*5
    namuzi=11-(sum_0 % 11)
    if namuzi == int(serial[13]):
        result = "검증완료"
    else:
        result = "부적격"
    return result

@app.route('/jumin', methods=['get','post'])
def create():
    if request.method == 'POST':
        jumin=request.form.get('jumin')

        if jumin.isalpha():
            return "문자가 포함되어 있어 검증이 불가합니다.14자리 숫자로 입력해주세요(예시: 010101-2020202)"

        # if jumin.isalpha():
        #     return "문자가 포함되어 있어 검증이 불가합니다.14자리 숫자로 입력해주세요(예시: 010101-2020202)"
        
        elif not len(jumin) == 14:
            return "입력하신 숫자가 부족하여 검증이 불가합니다. 14자리 숫자로 입력해주세요(예시: 010101-2020202)"
        return verify_jumin(jumin)
    
    return get_template('6.jumin.html')

app.run()