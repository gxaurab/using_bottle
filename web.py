#host a webapp on 5 lines of code
from bottle import run, route
@route('/gaurab') 
def func():
    return "GXAURAB"

run()

