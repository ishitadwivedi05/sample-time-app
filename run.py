from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    return f'The current time is: {current_time}'

if __name__ == '__main_':
    app.run(host='0.0.0.0', port=8080, debug=True)

