from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app=Flask(__name__)
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
    return render_template('home.html')

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
        return render_template('home.html')
    else:
        message="Enter correct details"
        return render_template('login.html',message=message)
    

@app.route('/add_user',methods=['POST'])
def add_user():
    email=request.form.get('email')
    phone=request.form.get('phone')
    password=request.form.get('password')

    cursor.execute("""INSERT into `user` (`userid`,`email`,`phone`,`password`) VALUES (NULL,'{}','{}','{}') """.format(email,phone,password))
    # cursor.execute(query)
    conn.commit()
    return "User registered successfully"


# print(__name__)
if __name__ == "__main__":
    app.run(debug=True)