from flask import Flask,render_template,request,redirect,url_for
import sqlite3
import os.path
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "hos.db")
if not os.path.exists(db_path):
    print("Database file not found!")
else:
    print("Database file exists.")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def hamada():
    return render_template('home.html')

# @app.route('/adminstrativee')
# def hamada():
#     username =request.form['user']
#     password = request.form['pass']
#     print("hamada")
#     print(username,password)
#     return render_template('adminstrative.html',username=username,password=password)



# =======================================
# this function to move me to the admistrative page
@app.route('/adminstrative')
def adminstrative():
    pw = "password"
    un = "username"
    return render_template('adminstrative.html',pw=pw,un=un)

# =================================================
# this function to chick if the admin is real or fake
@app.route('/adminstrativee',methods=['POST'])
def adminstratives():
    username = request.form['username']
    password = request.form['password']
    if username == "kirolos" and password == '123':
        message = "the registration is done"
        hidden = "hidden"
        truee = True
        return render_template('adminstrative.html',message = message,hidden=hidden,truee=truee,password=password)
    else:
        message = "the registration isn't successful\nplease enter the username or password again"
        pw = "password"
        un = "username"
        return render_template('adminstrative.html',message = message,un=un,pw=pw)
    # return render_template('adminstrative.html')


# =================================================
# this function move me form admin_diplay to admistrative
@app.route('/adminstrative2')
def adminstrativess():
    username = "kirolos"
    password = '123'
    if username == "kirolos" and password == '123':
        message = "the registration is done"
        hidden = "hidden"
        truee = True
        return render_template('adminstrative.html',message = message,hidden=hidden,truee=truee,password=password)
    
    # return render_template('adminstrative.html')


# ===================================================
# this function to insert a doctor
# ====================================================
@app.route('/adminstrativeee', methods=['POST'])
def sign():
    #this is connection with data base
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")

    hidden = "hidden"
    D_S_num = "surgy"
    D_ID = 1000
    rows_num = 1000
    D_Name = request.form['D_Name']
    D_Number = request.form['D_Number']
    D_Mail = request.form['D_Mail']
    D_Address = request.form['D_Address']
    D_Salary = request.form['D_Salary']
    D_Shift = request.form['D_Shift']
    D_Specialization = request.form['D_Specialization']
    if(D_Specialization == '1' ):
        D_S_num = "Surgery"
        D_ID =110000
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT MAX(CAST(SUBSTR(D_ID, -3) AS INTEGER)) AS max_last_3_digits FROM Doctors")
        # cur.execute('SELECT COUNT(*) FROM Doctors')
        rows_num = int(cur.fetchall()[0][0])
        rows_num = rows_num + D_ID +1
        print(rows_num)
    elif(D_Specialization == '2'):
        D_S_num = "Internal medicine"
        D_ID =120000
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT MAX(CAST(SUBSTR(D_ID, -3) AS INTEGER)) AS max_last_3_digits FROM Doctors")
        rows_num = int(cur.fetchall()[0][0])
        rows_num = rows_num + D_ID +1
        # cur.execute('SELECT COUNT(*) FROM Doctors')
        # rows_num = cur.fetchone()[0] + D_ID

    elif(D_Specialization == '3'):
        D_S_num = "Cardiology"
        D_ID =130000
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT MAX(CAST(SUBSTR(D_ID, -3) AS INTEGER)) AS max_last_3_digits FROM Doctors")
        rows_num = int(cur.fetchall()[0][0])
        rows_num = rows_num + D_ID +1
        # cur.execute('SELECT COUNT(*) FROM Doctors')
        # rows_num = cur.fetchone()[0] + D_ID

    elif(D_Specialization == '4'):
        D_S_num = "Ophthalmology"
        D_ID =140000
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT MAX(CAST(SUBSTR(D_ID, -3) AS INTEGER)) AS max_last_3_digits FROM Doctors")
        rows_num = int(cur.fetchall()[0][0])
        rows_num = rows_num + D_ID +1
        # cur.execute('SELECT COUNT(*) FROM Doctors')
        # rows_num = cur.fetchone()[0] + D_ID

    elif(D_Specialization == '5'):
        D_S_num = "Dental"
        D_ID =150000
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT MAX(CAST(SUBSTR(D_ID, -3) AS INTEGER)) AS max_last_3_digits FROM Doctors")
        rows_num = int(cur.fetchall()[0][0])
        rows_num = rows_num + D_ID +1
        # cur.execute('SELECT COUNT(*) FROM Doctors')
        # rows_num = cur.fetchone()[0] + D_ID

    elif(D_Specialization == '6'):
        D_S_num = "Specialization in neurosurgery"
        D_ID =160000
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT MAX(CAST(SUBSTR(D_ID, -3) AS INTEGER)) AS max_last_3_digits FROM Doctors")
        rows_num = int(cur.fetchall()[0][0])
        rows_num = rows_num + D_ID +1
        # cur.execute('SELECT COUNT(*) FROM Doctors')
        # rows_num = cur.fetchone()[0] + D_ID
    DA_ID = request.form['pass_admin']
    print(rows_num,D_Name,D_Number,"lalalala",D_Address,D_Salary,D_Shift,D_S_num)
    # conn = sqlite3.connect('database.db')


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
    conn = sqlite3.connect(db_path)

    cur = conn.cursor()
    cur.execute(''' INSERT INTO Doctors (D_ID, D_Name, D_Number, D_Mail, D_Address, D_Salary, D_Shift, D_Specialization, DA_ID) 
            VALUES (?,?,?,?,?,?,?,?,?)
        ''', (rows_num, D_Name, D_Number, D_Mail, D_Address, D_Salary, D_Shift, D_S_num, DA_ID))
    
    conn.commit()
    conn.close()
    mes ="the registration process is success"
    return render_template('adminstrative.html',mes=mes,hidden =hidden,t = True)


# ====================================================================
# this method to registration a patient
# ======================================================================
@app.route('/adminstrativeeee', methods=['POST'])
def signP():
    #this is connection with data base
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
        
    P_ID = 2000
    rows_num = 1000
    P_Name = request.form['P_Name']
    P_Number = request.form['P_Number']
    P_Mail = request.form['P_Mail']
    P_Address = request.form['P_Address']
    P_age = request.form['P_age']
    P_Gender = request.form['P_Gender']
        # D_Specialization = request.form['D_Specialization']
    if( P_Gender == "Male" ):
        P_ID =2100
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('SELECT MAX(P_ID) FROM Patients')
        rows_num = cur.fetchone()[0] + 1
    elif(P_Gender == "Female"):
        P_ID =2200
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('SELECT MAX(P_ID) FROM Patients')
        rows_num = cur.fetchone()[0] + 1
    
    PA_ID = request.form['pass_admin']
    # print(rows_num,D_Name,D_Number,"lalalala",D_Address,D_Salary,D_Shift,D_S_num)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
    conn = sqlite3.connect(db_path)

    cur = conn.cursor()
    cur.execute(''' INSERT INTO Patients (P_ID, P_Name, P_Number, P_Mail, P_Address, P_age, P_Gender, PA_ID) 
            VALUES (?,?,?,?,?,?,?,?)
        ''', (rows_num, P_Name, P_Number, P_Mail, P_Address, P_age, P_Gender, PA_ID))
    
    conn.commit()
    conn.close()
    mes ="the registration process is success"
    return render_template('adminstrative.html',mes=mes,hidden="hidden",t=True)



# ======================================================================
# this function to display the data for doctors by id
# ======================================================================

@app.route('/admin_display')
def admin_display():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('select * from Doctors')
    result = cur.fetchall()
    
    cur.execute('select * from Patients')
    result_p = cur.fetchall()
    
    conn.commit()
    conn.close()
    return render_template('admin_display.html',result=result,result_p = result_p)
        

# ======================================================
# to delet doctor 
# ======================================================
@app.route('/admin_delet/<id>')
def admin_delet(id):
    id = int(id)
    if id > 10000:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "hos.db")
        if not os.path.exists(db_path):
            print("Database file not found!")
        else:
            print("Database file exists.")

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('DELETE FROM Doctors WHERE D_ID = ?',(id,))
        if cur.rowcount == 0:
            mse  = "the delet process is fail "
            
        else:
            mse = "the delet process is doen "
        cur.execute('select * from Doctors')
        result = cur.fetchall()
        cur.execute('select * from Patients')
        result_p = cur.fetchall()
        conn.commit()
        conn.close()
        return redirect(url_for('admin_display', mse=mse, result=result, result_p=result_p))
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "hos.db")
        if not os.path.exists(db_path):
            print("Database file not found!")
        else:
            print("Database file exists.")
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('DELETE FROM Patients WHERE P_ID = ?',(id,))
        if cur.rowcount == 0:
            ms  = "the delet process is fail "
        else:
            ms = "the delet process is doen "
        cur.execute('select * from Doctors')
        result = cur.fetchall()
        cur.execute('select * from Patients')
        result_p = cur.fetchall()
        conn.commit()
        conn.close()
        return redirect(url_for('admin_display', ms=ms, result=result, result_p=result_p))
    

    
    


@app.route('/admin_update/<id>')
def admin_update(id):
    rows_num = int(id)
    if rows_num > 100000:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
        if not os.path.exists(db_path):
            print("Database file not found!")
        else:
            print("Database file exists.")
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('select * from Doctors where D_ID = ?',(rows_num,))
        result = cur.fetchall()
        conn.commit()
        conn.close()
        return render_template('update.html',result = result,doctor = True)
        # return redirect(url_for('update.html',result=result,doctor =True))
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
        if not os.path.exists(db_path):
            print("Database file not found!")
        else:
            print("Database file exists.")
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('select * from Patients where P_ID = ?',(rows_num,))
        result = cur.fetchall()
        conn.commit()
        conn.close()
        # return render_template('update.html',result = result,patient = True)
        return render_template('update.html',result=result,patient =True)



# ==============================================================
# this function to update doctor and patient
# ==============================================================
@app.route('/admin_update2', methods = ['POST'])
def admin_update2():
    D_ID = int(request.form['D_ID'])
    if D_ID > 100000:
        
        
        D_S_num = "surgy"
        
        rows_num = 1000
        D_Name = request.form['D_Name']
        D_Number = request.form['D_Number']
        D_Mail = request.form['D_Mail']
        D_Address = request.form['D_Address']
        D_Salary = request.form['D_Salary']
        D_Shift = request.form['D_Shift']
        D_Specialization = request.form['D_Specialization']
        if(D_Specialization == '1' ):
            D_S_num = "Surgery"
        elif(D_Specialization == '2'):
            D_S_num = "Internal medicine"
        elif(D_Specialization == '3'):
            D_S_num = "Cardiology"
        elif(D_Specialization == '4'):
            D_S_num = "Ophthalmology"
        elif(D_Specialization == '5'):
            D_S_num = "Dental"
        elif(D_Specialization == '6'):
            D_S_num = "Specialization in neurosurgery"
        DA_ID = request.form['pass_admin']

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
        if not os.path.exists(db_path):
            print("Database file not found!")
        else:
            print("Database file exists.")
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        
        cur.execute('''update Doctors set D_Name = ? ,D_Number = ?, D_Mail =?, D_Address =?, D_Salary =?, D_Shift =?, D_Specialization =? ,DA_ID = ? where D_ID =?
        ''',(D_Name, D_Number, D_Mail, D_Address, D_Salary, D_Shift, D_S_num, DA_ID , D_ID))
        if cur.rowcount == 0:
            messag_accept = "the udate process isn't done"
        else:
            messag_accept  = "the update process is done"
            print(D_ID)
        conn.commit()
        conn.close()
        return redirect(url_for('admin_display',messag_accept=messag_accept))
        # return render_template('home.html',ms =ms)
        # ===============================================================================
    else:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
        if not os.path.exists(db_path):
            print("Database file not found!")
        else:
            print("Database file exists.")

            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            P_ID = 2000
            rows_num = 1000
            P_Name = request.form['P_Name']
            P_Number = request.form['P_Number']
            P_Mail = request.form['P_Mail']
            P_Address = request.form['P_Address']
            P_age = request.form['P_age']
            P_Gender = request.form['P_Gender']
            PA_ID = request.form['pass_admin']

            cur.execute('''update Patients set P_Name = ? ,P_Number = ?, P_Mail =?, P_Address =?, P_age =?, P_Gender =?  ,PA_ID = ? where P_ID =?
            ''',(P_Name, P_Number, P_Mail, P_Address, P_age, P_Gender, PA_ID , D_ID))
            if cur.rowcount == 0:
                messag_accept = "the udate process isn't done"
            else:
                messag_accept  = "the update process is done"
                print(D_ID)
            conn.commit()
            conn.close()
            return redirect(url_for('admin_display',messag_accept=messag_accept))
            # return render_template('home.html',messag_accept=messag_accept)
    
    PA_ID = request.form['pass_admin']


# ==============================================================
# this function to move patient page
# ==============================================================
@app.route('/patient')
def patient():
    return render_template('patients.html')

# ==============================================================
# this function to login  patient by yourself
# ==============================================================
@app.route('/login_patient')
def login_patient():
    return render_template('patients.html',takedl = True,h = "hidden")


# ==============================================================
# this function to login  patient by yourself
# ==============================================================
@app.route('/login_patient2' , methods = ['POST'])
def login_patient2():
    
    username = request.form['username']
    P_ID = request.form['P_ID']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
    conn = sqlite3.connect(db_path)
    
    cur = conn.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM Patients WHERE P_ID = ?)",(P_ID,))
    exist = cur.fetchone()[0]
    if exist == 1:
        print(exist)
        cur.execute("select D_Name from Doctors")
        result = cur.fetchall()
        cur.execute("select * from Medicals where MP_ID =? ",(P_ID,))
        medicals = cur.fetchall()
        # print(medicals)
        mm = ' '
        consulting = True
        conn.commit()
        conn.close()
        return render_template('patients.html',consulting = consulting,h = "hidden",P_ID = P_ID,result =result,medicals = medicals ,mm =mm)

    else:
        mm = "this id is wrong please enter the id correctly"
        consulting = False
        return render_template('patients.html',consulting = consulting,mm =mm)

    # conn.commit()
    # conn.close()
    # return render_template('patients.html',consulting = consulting,h = "hidden",P_ID = P_ID,result =result,medicals = medicals ,mm =mm)


# ==============================================================
# this function to add consulting 
# ==============================================================
@app.route('/consulting', methods =['POST'])
def consulting():
    P_ID = request.form['P_ID']
    CD_Name = request.form['D_Name']
    C_Disctiption = request.form['C_Disctiption']
    print(type(C_Disctiption))
    C_Time = datetime.now()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT D_ID FROM Doctors WHERE D_Name = ?", (CD_Name,))
    result = cur.fetchone()
    
    if result:
        CD_ID = result[0]  # Extract the ID from the tuple
        print(CD_ID)
        cur.execute("INSERT INTO Consultings (C_Disctiption, C_Time, CP_ID, CD_ID) VALUES (?, ?, ?, ?)", 
                    (C_Disctiption, C_Time, P_ID, CD_ID))
        conn.commit()
    else:
        print("Doctor not found.")
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
    conn = sqlite3.connect(db_path)

    cur = conn.cursor()
    cur.execute("select D_Name from Doctors")
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return render_template('patients.html',consulting   = True,result=result,P_ID = P_ID,acceptance = "your consulting accepted")


# ==============================================================
# # this function to display a Medicals
# # ==============================================================
# @app.route('/' , methods = ['POST','GET'])
# def Doctor_display():
#     D_ID = 0
#     mse = ""
#     if request.method == 'GET':
#         D_ID =request.args.get('MD_ID')
#         mse = "the response is recorde"
#     else:
#         D_ID = request.form['D_ID']
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     db_path = os.path.join(BASE_DIR, "hos.db")
#     # Check if database file exists
#     if not os.path.exists(db_path):
#         print("Database file not found!")
#     else:
#         print("Database file exists.")
#     conn = sqlite3.connect(db_path)
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM Consultings where CD_ID = ? ',(D_ID,))
#     result = cur.fetchall()
#     if result:
#         print("kirolos fawzy kamel")
#         taked_DConsulting = True
#         ms =""
#         taked_Dl = False
#     else:
#         taked_DConsulting = False
#         ms = "your name or id isn't correct pleas enter again"
#         taked_Dl = True

#     conn.commit()
#     conn.close()
#     print(ms)
#     return render_template('Doctors.html',taked_DConsulting = taked_DConsulting,result = result,ms = ms,taked_Dl = taked_Dl,mse= mse)







# ==============================================================
# this function go to sign up patient page
# ==============================================================
@app.route('/sign_patient')
def sign_patient():
    return render_template('patients.html',takeds = True,he = "hidden")


# ==============================================================
# this function to sign up patient page by himsilf
# ==============================================================
@app.route('/sign_patient2', methods = ['POST'])
def sign_patient2():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
        
    P_ID = 2000
    rows_num = 1000
    P_Name = request.form['P_Name']
    P_Number = request.form['P_Number']
    P_Mail = request.form['P_Mail']
    P_Address = request.form['P_Address']
    P_age = request.form['P_age']
    P_Gender = request.form['P_Gender']
        # D_Specialization = request.form['D_Specialization']
    if( P_Gender == "Male" ):
        P_ID =2100
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('SELECT MAX(P_ID) FROM Patients')
        rows_num = cur.fetchone()[0] + 1
    elif(P_Gender == "Female"):
        P_ID =2200
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute('SELECT MAX(D_ID) FROM Doctors')
        rows_num = cur.fetchone()[0] + 1
    # print(rows_num,D_Name,D_Number,"lalalala",D_Address,D_Salary,D_Shift,D_S_num)
    conn.commit()
    conn.close()
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
    conn = sqlite3.connect(db_path)
    print(rows_num)
    cur = conn.cursor()
    cur.execute(''' INSERT INTO Patients (P_ID, P_Name, P_Number, P_Mail, P_Address, P_age, P_Gender) 
            VALUES (?,?,?,?,?,?,?)
        ''', (rows_num, P_Name, P_Number, P_Mail, P_Address, P_age, P_Gender))
    
    conn.commit()
    conn.close()
    mes ="the registration process is success"
    return render_template('patients.html',mes=mes,hidden="hidden")

    # return render_template('patients.html',takeds = True,he = "hidden")






# ==============================================================
# this function to move doctor page
# ==============================================================
@app.route('/Doctor')
def Doctor():
    return render_template('Doctors.html',taked_Dl = True)


# ==============================================================
# this function to display a consulting 
# ==============================================================
@app.route('/Doctor_display' , methods = ['POST','GET'])
def Doctor_display():
    D_ID = 0
    mse = ""
    if request.method == 'GET':
        D_ID =request.args.get('MD_ID')
        mse = "the response is recorde"
    else:
        D_ID = request.form['D_ID']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('SELECT * FROM Consultings where CD_ID = ? ',(D_ID,))
    result = cur.fetchall()
    if result:
        print("kirolos fawzy kamel")
        taked_DConsulting = True
        ms =""
        taked_Dl = False
    else:
        taked_DConsulting = False
        ms = "no consulting for this account !!"
        taked_Dl = True

    conn.commit()
    conn.close()
    print(ms)
    return render_template('Doctors.html',taked_DConsulting = taked_DConsulting,result = result,ms = ms,taked_Dl = taked_Dl,mse= mse)



# ==============================================================
# this function to to response on the consulting
# ==============================================================
@app.route('/doctor_Responce' , methods = ['POST'])
def doctor_Responce():

    MP_ID = request.form['CP_ID']
    MD_ID = request.form['CD_ID']
    C_Code = request.form['C_Code']
    # C_Code = request.form['C_Code']
    M_Disctiption = request.form['M_Disctiption']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "hos.db")
    
    # Check if database file exists
    if not os.path.exists(db_path):
        print("Database file not found!")
    else:
        print("Database file exists.")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    M_Doctor_Name = ''
    cur.execute("select D_Name from Doctors where D_ID = ?",(MD_ID,))
    result = cur.fetchone()
    print(result)
    if result:
        M_Doctor_Name = result[0]
        print("hamada el ya7sh")  # Extract the doctor's name from the tuple
    else:
        M_Doctor_Name = None
    cur.execute('DELETE FROM Consultings WHERE C_Code = ?',(C_Code,))
    cur.execute("insert into Medicals  (M_Disctiption , MP_ID , MD_ID ,M_Doctor_Name) values (?,?,?,?)",(M_Disctiption,MP_ID,MD_ID,M_Doctor_Name))
    conn.commit()
    conn.close()
    return redirect(url_for('Doctor_display',MD_ID=MD_ID))






# ==============================================================
# this function to display a consulting 
# ==============================================================
# @app.route('/Doctor_display2' , methods = ['GET'])
# def Doctor_display2():
#     D_ID =request.args.get('MD_ID')
#     BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#     db_path = os.path.join(BASE_DIR, "hos.db")
#     print(D_ID)
#     # Check if database file exists
#     if not os.path.exists(db_path):
#         print("Database file not found!")
#     else:
#         print("Database file exists.")
#     conn = sqlite3.connect(db_path)
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM Consultings where CD_ID = ? ',(D_ID,))
#     result = cur.fetchall()
#     if result:
#         print("kirolos fawzy kamel")
#         taked_DConsulting = True
#         ms =""
#         taked_Dl = False
#     else:
#         taked_DConsulting = False
#         ms = "your name or id isn't correct pleas enter again"
#         taked_Dl = True

#     conn.commit()
#     conn.close()
#     return render_template('Doctors.html',taked_DConsulting = taked_DConsulting,result = result,ms = ms,taked_Dl = taked_Dl)











# @app.route('/admin_update/<id>')
# def admin_update(id):
#     id = int(id)
#     if id > 10000:
#         BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#         db_path = os.path.join(BASE_DIR, "hos.db")
#         if not os.path.exi
# #         conn.close()
# #         return redirect(url_fsts(db_path):
#             print("Database file not found!")
#         else:
#             print("Database file exists.")

#         conn = sqlite3.connect(db_path)
#         cur = conn.cursor()
#         cur.execute('''update Doctors set D_Name = ? ,D_Number = ?, D_Mail =?, D_Address =?, D_Salary =?, D_Shift =?, D_Specialization =? where D_ID
# ''')
#         UPDATE your_table SET column1 = ?, column2 = ? WHERE condition_column = ?', (new_value1, new_value2, condition_value)
#         if cur.rowcount == 0:
#             mse  = "the delet process is fail "
            
#         else:
#             mse = "the delet process is doen "
#         cur.execute('select * from Doctors')
#         result = cur.fetchall()
#         cur.execute('select * from Patients')
#         result_p = cur.fetchall()
#         conn.commit()
#         conn.close()
#         return redirect(url_for('adminstrative', mse=mse, result=result, result_p=result_p))
#     else:
#         BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#         db_path = os.path.join(BASE_DIR, "hos.db")
#         if not os.path.exists(db_path):
#             print("Database file not found!")
#         else:
#             print("Database file exists.")
#         conn = sqlite3.connect(db_path)
#         cur = conn.cursor()
#         cur.execute('DELETE FROM Patients WHERE P_ID = ?',(id,))
#         if cur.rowcount == 0:
#             ms  = "the delet process is fail "
        # else:
#             ms = "the delet process is doen "
#         cur.execute('select * from Doctors')
#         result = cur.fetchall()
#         cur.execute('select * from Patients')
#         result_p = cur.fetchall()
#         conn.commit()or('adminstrative', ms=ms, result=result, result_p=result_p))

# ==============================================================
# admin_update patient
# ===============================================================
# @app.route('/admin_update/<id>')
# def admin_update(id):
#     rows_num = int(id)
#     if rows_num > 100000:
#         BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#         db_path = os.path.join(BASE_DIR, "hos.db")
    
#     # Check if database file exists
#         if not os.path.exists(db_path):
#             print("Database file not found!")
#         else:
#             print("Database file exists.")
#         conn = sqlite3.connect(db_path)
#         cur = conn.cursor()
        
#         result = cur.fetchall()
#         for row in result:
#             print(row+"\n")

#     # conn = sqlite3.connect(db_path)
#         cur.execute('select * from Patients')
#         result = cur.fetchall()
#         # for row in result_p:
#         #     print(row)
#         conn.commit()
#         conn.close()
#         return render_template('adminstrateive.html',result = result)

if __name__ == "__main__":
    app.run(debug=True)  