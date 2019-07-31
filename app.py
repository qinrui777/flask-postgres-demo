from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@127.0.0.1:5432/flask_demo'
db = SQLAlchemy(app)

db.create_all()

@app.route('/')
def index():
    return "<h1 style='color: red'>hellp flask postgres demo</h1>"

if __name__ == "__main__":
    app.run()