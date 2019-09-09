import json
from vernam import get_result
from operation_type import Operation
from flask import Flask, render_template, request
from jinja2 import Template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    form = request.form
    op = Operation[form['type'].upper()]
    result = get_result(op, form['message'], form['passphrase'])

    return json.dumps({
        "type": result.type_message,
        "msg": result.msg
    })

if __name__=="__main__":
    app.run()