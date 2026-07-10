import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    url = os.environ.get('URL_ZENO', '')
    return f'<iframe src="{url}" width="100%" height="100%" frameborder="0"></iframe>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
