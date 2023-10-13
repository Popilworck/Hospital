def getpid(pid):
    c.execute(f'select admid from doc_pat_details where pid = {pid} order by admid desc')
    return(c.fetchone()[0])
def getadid(adid):
    c.execute(f'select pid from doc_pat_details where admid = {adid}')
    return(idtoname(p=c.fetchall()[0][0]))
def getbid(bid):
    c.execute(f'select pid from bill where bid = {bid}')
    return(idtoname(p=c.fetchall()[0][0]))
def idtoname(s=None,p=None,admid=None):
    chong=[]
    if s!=None:
        q=f'select name from staff_data where sid = {s}'
        c.execute(q)
        chong.append(c.fetchall()[0][0])
    if p!=None:
        q=f'select name from patient_data where pid = {p}'
        c.execute(q)
        chong.append(c.fetchall()[0][0])
    if admid != None:
        idtoname(s,p)
    #print(chong)
    return chong[0]
def nametoid(p):
    c.execute(f'select pid from patient_data where name = "{p}"')
    return (c.fetchone()[0])
def nametoidd(p):
    c.execute(f'select sid from staff_data where name = "{p}"')
    return (c.fetchone()[0])
#------------------------------------------------------------------------------------------------------------
import mysql.connector,os,csv
from datetime import date
conn = mysql.connector.connect(host = 'localhost',user = 'root',password='2560',database = 'hospital')
c = conn.cursor()
conn.autocommit = True
l=os.getcwd()
#-------------------------------------------------------------------------------------------------------------
def addstaff(name,designation,pas):
    q='select sid from staff_data order by sid desc'
    c.execute(q)
    sid=c.fetchone()[0]+1
    q=f'insert into stff_data values({str(sid)},"{name}","{designation}")'
    c.execute(q)
    with open('logindata.csv','a',newline='') as f:
        csv.writer(f).writerow([name,sid,designation,pas])
    return(sid)
def remstaff(idd):
    q = f'delete from staff_data where sid={idd}'
    c.execute(q)
    try:
        chong = []
        with open("logindata.csv",'r') as f:
            for i in csv.reader(f):
                if idd in i:
                    continue
                else:
                    chong.append(i)
        with open("logindata.csv",'w',newline = '') as f:
            csv.writer(f).writerows(chong)
    except:pass
def showstaff():
    q = 'select name,sid from staff_data'
    c.execute(q)
    return(c.fetchall())
def showdoc():
    chong=[]
    q='select name from staff_data where designation = "doctor" order by sid'
    c.execute(q)
    for i in c.fetchall():
        chong.append(i[0])
    return(chong)
def updatestaff(sid,new,k):
    q = f'update staff_data set {k} = "{new}" where sid = {sid};' 
    c.execute(q)
    with open ('logindata.csv','r') as f:
        chong=[]
        for i in csv.reader(f):
            if sid in i:
                if k == 'name':
                    i[0]=new
                elif k=='sid':
                    i[1]=new
                else:
                    i[3]=new
                chong.append(i)
    with open ('logindata.csv','w',newline='') as f:
        csv.writer(f).writerows(chong)
def veiwcurrentpatients(sid):
    sid=str(sid)
    q = f'select pid from doc_pat_details where sid = {sid} and removed =0;'
    c.execute(q)
    chong = c.fetchall()
    ching=[]
    for i in chong:
        ching.append(idtoname(p=str(i[0])))
    return(ching)
def addpatient(pname,padd,pno,sid):
    q='select pid from patient_data order by pid desc'
    c.execute(q)
    pid=c.fetchone()[0]+1
    q= f'insert into patient_data values("{str(pid)}","{str(pname)}","{str(padd)}","{str(pno)}",0);' 
    c.execute(q)
    n='select admid from doc_pat_details order by admid desc'
    c.execute(n)
    admid=str(c.fetchone()[0]+1)
    q = f'insert into doc_pat_details(admid,sid,pid,doa,removed) values({admid},{str(sid)},{str(pid)},{str(date.today())},0);'
    c.execute(q)
def showallcurrentpatients():
    q = 'select pid,name from patient_data where removed =0'
    c.execute(q)
    return (c.fetchall())
def showallpatients():
    q = 'select pid,name from patient_data'
    c.execute(q)
    return (c.fetchall())
def viewpat(p):
    q = f'select * from doc_pat_details where pid = {p}'
    c.execute(q)
    chong=list(c.fetchall())
    #print(chong)
    ching=[]
    for i in chong:
        k=list(i)[:-1]
        q = f'select adress from patient_data where pid = {p}'
        c.execute(q)
        k.append(c.fetchall()[0][0])
        ching.append(k)
    return(ching)
def viewpatdoc(p):
    q = f'select pid,doa,ailment,medication,procedures from doc_pat_details where pid = {p}'
    c.execute(q)
    chong=list(c.fetchall())
    ching=[]
    for i in chong:
        k=list(i)
        k[0] = idtoname(p= k[0])
        ching.append(k)
    return(ching)
def updatepat_doc(sid,pid,update,new):
    q=f'update doc_pat_details set {update} = "{new}" where sid = {sid} and pid = {pid} and removed = 0;'
    c.execute(q)
def removepatient(pid):
    try:
        q0=f'update doc_pat_details set dod = "{date.today()}" where pid ={pid};'
        q1=f'update doc_pat_details set removed = 1 where pid = {pid} ;'
        q2=f'update patient_data set removed = 1 where pid = {pid};'
        for i in range(3):
            exec(f'c.execute(q{i})')
    except Exception as e:print(e)
def getinfo(inf,pid,sid):
    q=f'select {inf} from doc_pat_details where pid = {pid} and sid = {sid}'
    c.execute(q)
    return(c.fetchone()[0])
def setinfo(inf,pid,info,sid):
    q=f'update doc_pat_details set {inf} = "{info}" where pid = {pid} and sid = {sid}'
    c.execute(q)
def getinfos(inf,sid):
    q=f'select {inf} from staff_data where sid = {sid}'
    c.execute(q)
    return(c.fetchone()[0])
def setinfos(inf,info,sid):
    q=f'update staff_data set {inf} = "{info}" where sid = {sid}'
    c.execute(q)
if __name__ == '__main__':
    #print(c.execute('select sid from staff_data').fetchall())
    removepatient(966)