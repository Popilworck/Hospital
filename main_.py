import mysql.connector,csv
import loginpage,signuppage,adminmenuv2,docmenuv2
password = ''#Enter password here
def onest():
        conn1 = mysql.connector.connect(username='root',host='localhost',password=password,database = 'world')
        conn1.autocommit = True
        c1 = conn1.cursor()
        c1.execute('create database if not exists trial;')
def twond():
    conn2 = mysql.connector.connect(username='root',host='localhost',password=password,database = 'trial')
    conn2.autocommit = True
    c2= conn2.cursor()
    q1='CREATE TABLE if not exists patient_data (pid int NOT NULL AUTO_INCREMENT,name varchar(255) NOT NULL,adress varchar(255) DEFAULT NULL,phoneno varchar(10) DEFAULT NULL,removed tinyint NOT NULL DEFAULT 0,PRIMARY KEY (pid));'
    q2='CREATE TABLE if not exists staff_data (sid int NOT NULL AUTO_INCREMENT,name varchar(255) NOT NULL,designation varchar(255) NOT NULL DEFAULT "doctor",adress varchar(255) DEFAULT NULL,phoneno char(10) DEFAULT NULL,salary int NOT NULL,emailid varchar(255) DEFAULT NULL,PRIMARY KEY (sid));'
    q3='CREATE TABLE if not exists doc_pat_details (admid int NOT NULL AUTO_INCREMENT,sid int NOT NULL,pid int NOT NULL,doa date NOT NULL,dod date DEFAULT NULL,ailment varchar(255) DEFAULT NULL,medication varchar(255) DEFAULT NULL,procedures varchar(255) DEFAULT NULL,removed tinyint DEFAULT NULL,PRIMARY KEY (admid),KEY sid (sid),KEY pid (pid),CONSTRAINT doc_pat_details_ibfk_1 FOREIGN KEY (sid) REFERENCES staff_data (sid),CONSTRAINT doc_pat_details_ibfk_2 FOREIGN KEY (pid) REFERENCES patient_data (pid))'
    for i in range(1,4):
        exec(f'c2.execute(q{i})')
def threerd():
    conn3 = mysql.connector.connect(username='root',host='localhost',password=password,database = 'trial')
    conn3.autocommit = True
    c3 = conn3.cursor()
    for j in ['doc_data.csv','patient_data.csv','data_data.csv']:
        with open(j,'r') as f:
            for i in csv.reader(f):
                if i[0].isdigit()==True:
                    q=f'insert into staff_data values {tuple(i)}' if j == 'doc_data.csv' else f'insert into patient_data values {tuple(i)} ' if j=='patient_data.csv' else f'insert into doc_pat_details values {tuple(i)}'
                    c3.execute(q)
#lpm = ('','',True,)prof,id,quartz
lpm = ('','',True,'opened')
def start(): 
    global lpm
    lpm = loginpage.main()
    if lpm[0]!='':
        if lpm[0] != 'doctor':
            adminmenuv2.patmain(lpm[1])
        elif lpm[0] == 'doctor':
            docmenuv2.main(lpm[1])
    else:
        if lpm[3] != 'closed':
            start()
def admen():
    adminmenuv2.patmain(lpm[1])
def ad():
    signuppage.main()
def docmen():
    docmenuv2.main(lpm[1])
if __name__=='__main__':
    start()