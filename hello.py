# -*- coding:utf-8
"""
@Created on 2018/1/6 22:57
@Author: Pengjiaxin
"""

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return [b'<h1>Hello, web!</h1>']
#
import os
path = "./template"
os.chdir(path)

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("qipan.html")

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()