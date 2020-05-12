# 원의 원주율을 구해보자
# /pi


from flask import Flask, request
import math

app=Flask(__name__)
app.env="development"
app.debug=True


@app.route('/pi')
def pi():
    diameter=2
    polygon=6
    side=1
    n=15

    result = ["원의 원주율 구하기"]

    for i in range(n):
        polygon = polygon *2
        side = (2-(4-side**2)**.5)**.5
        pi = side * polygon /diameter
        result.append("{0}각형 : {1}".format(polygon,pi))

    return '<br>'.join(result)

app.run()