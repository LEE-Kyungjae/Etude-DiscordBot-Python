from flask import Flask
app = Flask(__name__)

a = 0

@app.route('/')
def home():
    a=1
    return 'This is Home!<br><p>gg</p><input type=text>'

if __name__ == '__main__':  
    a=2
    app.run('0.0.0.0',port=5000,debug=True)