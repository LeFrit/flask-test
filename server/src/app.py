from flask import Flask, render_template
import os
import time

app = Flask(__name__)

def format_time():
    local_time = time.localtime()
    return time.strftime("%I:%M:%S %p", local_time)

@app.route('/')
def index():
    context = {
        "local_time": format_time()
    }
    return render_template('index.html', context=context)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
