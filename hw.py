    
from flask import Flask

app = Flask(__name__)

@app.route('/<int:cm>')

def cm_in(cm):
    inch = cm * 0.394
    return f'{inch}'


if __name__=='__main__':
    app.run()
