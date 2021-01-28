import json
import datetime
from vernam import get_result
from operation_type import Operation
from flask import Flask, render_template, request
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', year=datetime.datetime.now().year)

@app.route('/start', methods=['POST'])
def start():
    form = request.form
    op = Operation[form['type'].upper()]
    result = get_result(op, form['message'], form['passphrase'])

    return json.dumps({
        "type": result.type_message,
        "msg": result.msg
    })

@app.route('/hello', methods=['GET'])
def me():
    bd = datetime.datetime.strptime('11/04/1989 00:00:00', '%d/%m/%Y %H:%M:%S')
    now = datetime.datetime.now()
    total = now - bd
    days = total.days
    
    return render_template('me.html', year=datetime.datetime.now().year, age=days//365)

if __name__=="__main__":
    app.run()