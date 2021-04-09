import SignLaguage
from flask import  Flask
app= Flask(__name__)

@app.route('/')
def Welcome():
    return "Hello"

@app.route('/sign/')
def signlanguage():
    return exec('SignLanguage.py')

if __name__=="__main__":
    app.run()