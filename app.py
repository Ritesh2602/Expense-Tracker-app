from flask import Flask,render_template

app=Flask(__name__)


# decorator
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


# print(__name__)
if __name__ == "__main__":
    app.run(debug=True)