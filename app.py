import os
from flask import Flask,render_template

app = Flask(__name__)
color = "red"

@app.route('/')
def hello_world():
     color = 'red'
     color_fun_v = color_fun()
     if color_fun_v!='':
         color=color_fun_v
     print(color)
     return render_template('index.html', color=color)

def color_fun():
    try:
        return os.environ["color"]
    except KeyError:
        return ''

if __name__ == '__main__':
    app.run()
