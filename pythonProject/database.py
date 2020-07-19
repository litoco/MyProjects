import sqlite3
con = sqlite3.Connection('rdb')
cur = con.cursor()
c=1
cusid=0
def insert(s):
    global c
    c = 1
    cur.execute("create table if not exists customerorder(no number,menuitems varchar(40))")
    cur.execute("create table if not exists customerorder2(no number,menuitems varchar(40))")
##    cur.execute("select no from customerorder order by no desc")
##    l=cur.fetchall()
##    if(l==[]):
##        c = 1
##    else:
##        c = l[0][0] + 1
    for i in s:
        cur.execute("insert into customerorder values(?,?)",(int(c),i))
        cur.execute("insert into customerorder2 values(?,?)",(int(c),i))
        con.commit()
        c+=1
def fetch(s):
    global c
    cur.execute("select * from customerorder2 where no between ? and ?",(c-len(s),c-1))
    l = cur.fetchall()
    cur.execute("DROP TABLE customerorder2")
    return l

def insertall(s1):
    global cusid
    cur.execute("create table if not exists customerdetails(cid number primary key,fullname varchar(20),mobno number(10),address varchar(100))")
    cur.execute("select cid from customerdetails order by cid desc")
    l=cur.fetchall()
    if(l==[]):
        cusid = 1
    else:
        cusid = l[0][0] + 1
    b=(int(cusid),(s1[0]),int(s1[1]),(s1[2]))
    cur.execute('insert into customerdetails values(?,?,?,?)',b)
    con.commit()
def fetchall():
     global cusid
     cur.execute('select * from customerdetails where cid = ?',(cusid,))
     #cur.execute('select * from customerdetails')
     return list(cur.fetchall())
