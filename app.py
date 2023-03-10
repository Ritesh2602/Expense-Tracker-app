from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)
conn = mysql.connector.connect(
   user='root', password='', host='127.0.0.1', database='login'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# decorator
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    if 'user_id' in session:
        return render_template('home.html')
    else:
        return redirect('/')

@app.route('/login_validation', methods=['POST','GET'])

def login_validation():
    message=''
    email=request.form.get('email')
    password=request.form.get('password')

    query=(""" Select * from `user` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """.format(email,password))
    cursor.execute(query)
    user=cursor.fetchall()
    # print(user)
    # return user

    if user:
        session['user_id']=user[0][0]
        return redirect('/home')
    else:
        message="Enter correct details"
        return redirect('/',message=message)
    

@app.route('/add_user',methods=['POST'])
def add_user():
    email=request.form.get('email')
    phone=request.form.get('phone')
    password=request.form.get('password')

    cursor.execute("""INSERT into `user` (`userid`,`email`,`phone`,`password`) VALUES (NULL,'{}','{}','{}') """.format(email,phone,password))
    # cursor.execute(query)
    conn.commit()
    return "User registered successfully"


@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


# print(__name__)
if __name__ == "__main__":
    app.run(debug=True)