import json
import datetime
import os
from tt_api import TikTokWrapper
from validator import Validator
from vernam import get_result
from operation_type import Operation
from flask import Flask, render_template, request, send_from_directory, current_app

app = Flask(__name__)
app.config.from_file(os.path.join(os.getcwd(), 'config.json'), load=json.load)
base_url = app.config["BASE"]

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

@app.route('/video', methods=['GET'])
def video():
    validator = Validator()
    token = request.headers['x-auth-token']
    if not validator.validate(token):
        return 'Not Authorized', 401

    uploads = os.path.join(current_app.root_path, 'uploads')
    video_id = request.args.get('id')
    video_name = f'v{video_id}.mp4'

    if os.path.isfile(os.path.join(uploads, video_name)):
        return f'{base_url}/uploads/{video_name}'
    
    wrapper = TikTokWrapper()
    video_bytes = wrapper.get_video(video_id)
    
    with open(os.path.join(uploads, video_name), "wb") as out_file:
        out_file.write(video_bytes)

    return f'{base_url}/uploads/{video_name}'

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(current_app.root_path, 'uploads')
    return send_from_directory(uploads, filename)

if __name__ == "__main__":
    app.run()