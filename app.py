import sqlite3
from flask import Flask,render_template,request,url_for

app = Flask(__name__)

conn = sqlite3.connect('my_db.db')  
cur = conn.cursor()
# Drop the student table if already exists.
cur.execute("DROP TABLE IF EXISTS STUDENT")

    # Creating table
conn.execute('CREATE TABLE Student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, addr TEXT, city TEXT, pin TEXT)')

@app.route('/')
def home():
    
    
    return  render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student.html')    

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      #try:
         name = request.form.get('nm')
         addr = request.form.get('add')
         city = request.form.get('city')
         pin = request.form.get('pin')
         
         conn = sqlite3.connect('my_db.db')  
            
         cur = conn.cursor() #It is an object that is used to make the connection for executing SQL queries. It acts as middleware between SQLite database connection and SQL query.
         cur.execute("INSERT INTO Student (name,addr,city,pin) VALUES (?,?,?,?)",(name,addr,city,pin))
         conn.commit()  
         msg = "Student successfully Added"  
         return render_template("result.html",msg = msg)
         conn.close()

@app.route('/list')
def list():
   
   
    conn = sqlite3.connect('my_db.db')  
    conn.row_factory = sqlite3.Row  
    cur = conn.cursor()  
    cur.execute("select * from Student")  
    rows = cur.fetchall()  
    return render_template("list.html",rows = rows)  

@app.route('/del_student')
def del_student():
    conn = sqlite3.connect('my_db.db')  
      
    cur = conn.cursor()  
    cur.execute("delete from Student")
    conn.commit()    
    return render_template("list.html") 

@app.route('/updatestudent')
def updatestudent():
   return render_template('update_student.html') 


@app.route('/update_student',methods = ['POST', 'GET'])
def update_student():
    if request.method == 'POST':
      #try:
         id=request.form.get('id')
         nm = request.form.get('nm')
         addr = request.form.get('add')
         city = request.form.get('city')
         pin = request.form.get('pin')
         
         conn = sqlite3.connect('my_db.db')  
         mydata=(nm,addr,city,pin,id) 
         q="UPDATE Student set name=?,addr=?,city=?,pin=?  WHERE id=? "
         r_set=conn.execute(q,mydata)
         
         conn.commit()    
         msg = "Student successfully updated"  
         return render_template("result.html",msg = msg)
         conn.close()


if __name__ == '__main__':
   app.run() 
