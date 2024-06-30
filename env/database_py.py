import sqlite3

conn = sqlite3.connect('datebase.db')
if(conn):
    print("the connection is done")
cur = conn.cursor()
# cur.execute('''
#             create table Adminstratives(
#             A_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             A_Name TEXT,
#             A_Number text,
#             A_Mail text,
#             A_Address text,
#             A_Salary text)
#             ''')
# =================================================
# cur.execute('''
#             create table Patients(
#             P_ID integer primary key,
#             P_Name text,
#             P_Number text,
#             P_Mail text,
#             P_Address text,
#             P_age text,
#             P_Gender text,
#             PA_ID integer,
#             foreign key (PA_ID) references Adminstratives (A_ID)
#             )
#             ''')
# cur.execute('''
#             create table Doctors(
#             D_ID integer primary key,
#             D_Name text,
#             D_Number text,
#             D_Mail text,
#             D_Address text,
#             D_Salary text,
#             D_Shift text,
#             D_Specialization text,
#             DA_ID integer,
#             foreign key (DA_ID) references Adminstratives (A_ID)
#             )
#             ''')
# ====================================
# cur.execute('''
#             create table Consultings(
#             C_Code integer primary key autoincrement,
#             C_Disctiption text,
#             CP_ID integer, 
#             CD_ID integer, 
#             C_Time,
#             foreign key (CP_ID) references Patients (P_ID),
#             foreign key (CD_ID) references Doctors (D_ID)
#             )
#             ''')
# ======================================
# cur.execute('''
#             create table Medicals(
#             M_Code integer primary key autoincrement,
#             M_Disctiption text,
#             MP_ID integer, 
#             MD_ID integer, 
#             foreign key (MP_ID) references Patients (P_ID),
#             foreign key (MD_ID) references Doctors (D_ID)
#             )
#             ''')
# ==============================
# cur.execute('''
#             alter table Medicals 
#             add column M_Doctor_Name text
# ''')
# cur.execute('''
#             INSERT INTO Doctors (D_ID, D_Name, D_Number, D_Mail, D_Address, D_Salary, D_Shift, D_Specialization, DA_ID) 
#             VALUES 
#          (124, "kirosls", "fahd", "kiro", "kiro", "kiro", "kiro", "kiro", 123)''')
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "hos.db")
if not os.path.exists(db_path):
    print("Database file not found!")
else:
    print("Database file exists.")

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute('DELETE FROM  Medicals WHERE M_Code in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,31,34,35,36,37,33,41,45,46,47,48,49)')
cur.execute('''SELECT MAX(CAST(SUBSTR(D_ID, -3) AS INTEGER)) AS max_last_3_digits
FROM Doctors''')
result = cur.fetchall()[0][0]
print(result)
conn.commit()
conn.close()
