import sqlite3
import re
import os
import datetime
from forms import foorms
class models():
    def check(self):
        l=[]
        fo=foorms()
        con=sqlite3.connect('blog.db')
        a=con.execute('select EMAIL FROM USER')
        for each in a:
            l.append(each[0])
       
        if fo.logi.data in l:
            b=con.execute('SELECT PASSWORD FROM USER WHERE EMAIL=?',(fo.logi.data,))
            for each in b:
                
                l.append(each[0])
            
            if fo.pasw.data in l:
                return'ok'
            else:
                return 'pw'
     
        return 'u'
    def addd(self):
        fo=foorms()
        con = sqlite3.connect('blog.db')
        con.execute("INSERT INTO USER(NAME,EMAIL,PASSWORD) \
                VALUES(?,?,?)",(fo.name.data,fo.l.data,fo.p.data));
        con.commit()
       
        return 'Saved'
    def search(self,pat):
        l=[]
        fo=foorms()
       
        con=sqlite3.connect('blog.db')
        b=con.execute('select POST from posts')
        for each in b:
            each=str(each[0])
            
            match=re.search(pat,each,re.IGNORECASE)
            if match:
                a=con.execute('select status from posts where post=?',(each,))
                for i in a:
                    if i[0]=='publish':
                        l.append(each)
        if len(l)==0:
            return 'nom'
        return l
    def parag(self,l):
       b={}
       con=sqlite3.connect('blog.db')
       for each in l:
            d=con.execute('select PL from posts where POST=?',(each,))
            for i in d:
                r=open('app'+'/'+'blogs'+'/'+i[0])
                r=r.readlines()
                b[each]=r[0]
       return b
    def date(self,l):
       b={}
       con=sqlite3.connect('blog.db')
       for each in l:
            d=con.execute('select DATE from posts where POST=?',(each,))
            for i in d:
                b[each]=i[0]
                break
       return b
    def name(self,l):
        b={}
        con=sqlite3.connect('blog.db')
        for each in l:
            d=con.execute('select NAME from posts where POST=?',(each,))
            for i in d:
                b[each]=i[0]
                break
        return b 
    def namecheck(self,p):
        fo=foorms()
        con=sqlite3.connect('blog.db')
      
        d=con.execute('select NAME from USER where EMAIL=?',(p,))
        
        for each in d:
            
            return each[0]
    def findp(self,p):
        l=[]
        con=sqlite3.connect('blog.db')
        d=con.execute('select post from posts where name=?',(p,))
        for each in d:
            
            l.append(each[0])
        return l
    def findpf(self,p):
        l=[]
        con=sqlite3.connect('blog.db')
        d=con.execute('select post from posts where pl=?',(p,))
        for each in d:
            
            l.append(each[0])
        return l
    def status(self,po):
        b={}
        con=sqlite3.connect('blog.db')
        for each in po:
            d=con.execute('select status from posts where POST=?',(each,))
            for i in d:
                 b[each]=i[0]
                 break
        return b
    def pl(self,po):
        b={}
        con=sqlite3.connect('blog.db')
        for each in po:
            d=con.execute('select pl from posts where POST=?',(each,))
            for i in d:
                 b[each]=i[0]
                 break
        return b
    def addc(self,n,p):
      
        fo=foorms()
        time=datetime.datetime.now().time()
        con=sqlite3.connect('blog.db')
        a=con.execute('select comment,cn from posts where post=?',(p,))
        for i,j in a:
            x=i
            y=j+1
            f=open('app'+'/'+'command'+'/'+str(time),'a')
            
        
            f.write(n)
            now=datetime.date.today()
            con.execute('insert into comments (post,com,date) \
                   VALUES(?,?,?)',(i,str(time),str(now.day)+'/'+str(now.month)+'/'+str(now.year)))
            con.commit()
        
            con.execute('update posts set cn=:j where comment=:i',{'j':y,'i':x})
            con.commit()           
   
    def publish(self,p,status):
        con=models()
        po=con.findp(p)
        fo=foorms()
        now=datetime.datetime.now()
        time=datetime.datetime.now().time()  
        con=sqlite3.connect('blog.db')
        l=str(fo.head.data)
        
        if l in po:
            print 'll'
            con.execute('delete from posts where post=?',(l,))
            con.commit()
        f=str(fo.head.data)
        if status=='create':
            con.execute('insert into posts(NAME,POST,PL,COMMENT,CN,DATE,STATUS) \
                    VALUES(?,?,?,?,?,?,?)',(p,f,str(time),f[:5],0,str(now.day)+'/'+str(now.month)+'/'+str(now.year),'publish'))
            con.commit()
          
            d=open('app'+'/'+'blogs'+'/'+str(time),'w')
         
            d.write(fo.body.data)
            d.close()
        elif status=='save':
            con.execute('insert into posts(NAME,POST,PL,COMMENT,CN,DATE,STATUS) \
                    VALUES(?,?,?,?,?,?,?)',(p,f,str(time),f[:5],0,str(now.day)+'/'+str(now.month)+'/'+str(now.year),'save'))
            con.commit()       
          
            d=open('app'+'/'+'blogs'+'/'+time,'w')
            d.write(fo.body.data)
            d.close()
    def ret(self,po):
        f=foorms()
        con=sqlite3.connect('blog.db')
        k=[]
        
        b=con.execute('select pl from posts where post=?',(po,))
        for each in b:
          a=open('app'+'/'+'blogs'+'/'+each[0])
         
          k=a.readlines()
        return k
    def dele(self,po):
        fo=foorms()
        con=sqlite3.connect('blog.db')
        d=con.execute('select pl from posts where post=?',po)
        for each in b:
          os.remove('blogs'/each)
          break
        con.execute('delete from posts where post=?',po)
    def comret(self,po):
        fo=foorms()
        con=sqlite3.connect('blog.db')
     
        c={}
        z=[]
        
        d=con.execute('select com,date from comments where post=?',(po[0][:5],))
        for i,j in d:
                
            c[i]=j
            o=open('app'+'/'+'command'+'/'+i)
            z.append((i,o.readlines()))
          
        return (c,z) 
    def delcom(self,po):
        fo=foorms()
        con=sqlite3.connect('blog.db')
         
        con.execute('delete from comments where com=?',(po,))
        con.commit()    
        os.remove('app'+'/'+'command'+'/'+po)
      
