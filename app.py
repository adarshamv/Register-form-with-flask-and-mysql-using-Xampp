from flask import Flask,render_template,request
import mysql.connector


app=Flask(__name__)
@app.route('/')
def student():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="flask"
    )
    mycursor=mydb.cursor()
    if request.method=='POST':
        signup=request.form
        username=signup['user']
        email=signup['email']
        mobile=signup['mob']
        password=signup['password']
        rpassword=signup['rpass']
        mycursor.execute("insert into reg (user,email,mob,pass,rpass) values(%s,%s,%s,%s,%s)",(username,email,mobile,password,rpassword))
        mydb.commit()
        mycursor.close()
        return "Register successful"



if __name__=="__main__":
    app.run(debug=True)

