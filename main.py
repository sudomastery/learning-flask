from flask import Flask
#from about_me import bp as about_bp
from hobbies import bp as hobbies_bp

app = Flask(__name__)
#app.register_blueprint(about_bp)
app.register_blueprint(hobbies_bp)



@app.route('/')
def home():
    return '<h1>Landing Page</h1>'

