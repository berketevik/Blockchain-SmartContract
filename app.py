from flask import Flask , render_template,request,redirect,url_for,json,flash
from flask_mysqldb import MySQL
from pymysql.cursors import DictCursor#TO FETCH AS DICTIONARY

app= Flask(__name__)

#CONFIGURE DATABASE
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='hotel'
mysql = MySQL(app)
#THIS IS FOR TO USE flask.flash() METHOD
app.secret_key='12345'

##FIRST PAGE
@app.route("/")
def firstPage():
    return redirect(url_for("signup"))#signup fonksiyonuna yonlendirdi
##SIGNUP
@app.route("/signup.html",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        req=request.form
        username=req.get("username")
        email=req.get("email")
        password=req.get("password")
        print(username,email,password)
        if not len(password) >= 1:
            flash("Password must be at least 10 characters in length","danger")#For bootstrap changes
            return redirect(request.url)#render ayni html adresinde farkli bir html sayfasi goruntuleyebilir   
        #flash("sign in succesfull","danger")#For bootstrap changes
        return redirect("/info.html")#Belirtilen sayfaya veya fonksiyona gonderir adresi degistirir
    return render_template("/signup.html")
#INFO HTML
@app.route("/info.html")
def info():
    return render_template("/info.html")
##ROOMS
@app.route("/rooms.html",methods = ["GET","POST"])
def room():
    cur=mysql.connection.cursor()#CURSOR
    if request.method == "POST":
        if request.form['submit_button'] == 'submit':
            return render_template("/payment.html")
    else:
        resultValue=cur.execute("select * from room")#taking all room info
        ##CONTROL IF THERE ARE ANY DATA EXIST 
        if resultValue>0:
            results=cur.fetchall()
            return render_template("/rooms.html",results=results)


#TO RUN OUR PYTHON APP
if __name__ =="__main__":
    app.run(debug=True)