from flask import Flask,render_template,flash,redirect,request,session,url_for
from app import app
from model import *
from forms import foorms
@app.route('/login/',methods=['GET','POST'])
def login():
    fo=foorms()
    con=models()
    if request.method=='POST':
        if request.form['add']=='login':
            current=str(fo.logi.data)
            session['current']=current
            s=con.check()
            if s=='ok':
                
                return redirect(url_for('.user',current=current))
            elif s=='u':
                flash('Invalid Email')
                
            elif s=='pw':
                flash('Wrong Password')
        if request.form['add']=='signup':
            return redirect('/signup')
        if request.form['add']=='search':
            se=fo.sear.data
            session['se']=se
            tmp='no'
            session['tmp']=tmp
            return redirect(url_for('.search',se=se,tmp=tmp))
    return render_template('login.html',fo=fo)
@app.route('/signup/',methods=['GET','POST'])
def signup():
    fo=foorms()
    con=models()
    if request.method=='POST':
        if request.form['add']=='signup':
            s=con.addd()
            
            flash(s)   
        if request.form['add']=='login':
            return redirect('/login')
    return render_template('signup.html',fo=fo)
@app.route('/search/',methods=['GET','POST'])
def search():
    fo=foorms()
    con=models()
    se=session['se']
    p=con.search(se)
    tmp=session['tmp']
    
    f=''
    d=''
    n=''
    pp=''

    if p=='nom':
        p=''
        flash('NO MATCH FOUND')
    else:
        pp=con.pl(p)
        f=con.parag(p)
        d=con.date(p)
        n=con.name(p)
    	if request.method=='POST':
                b=request.form.keys()[0]
                     
        	if request.form[b]=='Read More':
                       
                    session['b']=b
                    session['tmp']=tmp          
        	    return redirect(url_for('.blog',b=b,tmp=tmp))
                
    return render_template('search.html',fo=fo,p=p,f=f,d=d,n=n,pp=pp)
@app.route('/user/',methods=['GET','POST'])
def user():
    fo=foorms()
    con=models()

    current=session['current']
    p=con.namecheck(current)
    po=con.findp(p)
    d=con.date(po)
    
    #f=con.parag(po)
    session['p']=p
    session['po']=po
    session['d']=d
   
    s=con.status(po)
    session['s']=s
    pp=con.pl(po)
    
  
    
    if request.method=='POST':
        b=request.form.keys()[0]
             
        if request.form[b]=='edit':
            z='no'
            session['z']=z
            pf=con.findpf(b)
            session['pf']=pf           
            return redirect(url_for('.create',p=p,pf=pf,z=z))
        if request.form[b]=='view':
            session['b']=b
            return redirect(url_for('.reply',b=b))
    if request.method=='POST':
       
        if request.form['add']=='create':
            z='yes'
            session['z']=z
            print 'p',p,po                   
            return redirect(url_for('.create',p=p,po=po,z=z))
        if request.form['add']=='search':
            se=fo.sea.data
            tmp='yes'
            session['tmp']=tmp
            session['se']=se
            return redirect(url_for('.search',se=se,tmp=tmp))
        if request.form['add']=='logout':
            return redirect('/login/')
    return render_template('posts.html',fo=fo,p=p,pp=pp,po=po,d=d,s=s) 
@app.route('/blog/',methods=['GET','POST'])
def blog():
    fo=foorms()
    con=models()
    tmp=session['tmp']
    b=session['b']
    
    pf=con.findpf(b)
    
    a=open('app'+'/'+'blogs'+'/'+b)
    k=a.readlines()
    h=con.comret(pf)
    
    z=h[1]
    c=h[0]    
    if request.method=='POST':
     
        if request.form['add']=='submit':
         
            con.addc(fo.com.data,pf[0])
            session['b']=b
            return redirect(url_for('.blog',b=b))
        if request.form['add']=='home':
           
            if tmp=='no':return redirect('/login/')
            else:return redirect('/user/')
        if request.form['add']=='logout':
            return redirect('/login/')
    return render_template('blog.html',fo=fo,k=k,pf=pf,tmp=tmp,z=z,c=c)
@app.route('/create/',methods=['GET','POST'])
def create():
    l=[]
    k=''
    
    fo=foorms()
    fo.body.data=''
    con=models()
    #po=request.args['po']
    p=session['p']
    pf=session['pf']
  
    z=session['z']
    if z=='no':
        k=pf[0]
        l=con.ret(pf[0])
        if len(l)>0:
            for each in l:
                fo.body.data+=each
    if request.method=='POST':
       
        if request.form['add']=='refresh':
            k=''
            fo.body.data=''    
        if request.form['add']=='save':
            con.publish(p,'save')
            k=fo.head.data
            l=con.ret(fo.head.data)
            fo.body.data=''
            if len(l)>0:
                for each in l:
                    fo.body.data+=each
        if request.form['add']=='publish':
            con.publish(p,'create')
            k=fo.head.data
            l=con.ret(fo.head.data)
            fo.body.data=''
            if len(l)>0:
                for each in l:
                    fo.body.data+=each
        if request.form['add']=='home':
            return redirect('/user/')
        if request.form['add']=='logout':
            return redirect('/login/')        
    return render_template('create.html',fo=fo,pf=pf,k=k)
@app.route('/reply',methods=['GET','POST'])
def reply():
    fo=foorms()
    con=models()
    b=session['b']
 
    pf=con.findpf(b)
  
    a=open('app'+'/'+'blogs'+'/'+b)
    k=a.readlines()
    h=con.comret(pf)
    
    c=h[0]
    z=h[1]
    
     
    if request.method=='POST':
        p=request.form.keys()
        
        for each in p:
            if request.form[each]=='delete':
                   
                con.delcom(each)
                session['b']=b
                return redirect(url_for('.reply',b=b))
    if request.method=='POST':
        if request.form['add']=='submit':
            a=fo.rly.data
            if a!='': 
                f=open('app'+'/'+'command'+'/'+a[:3],'a')
                f.write('Reply\n\n')
                f.close()
                con.addc(a,pf[0])
                session['b']=b
                return redirect(url_for('.reply',b=b))
        if request.form['add']=='home':
            return redirect('/user/')
        if request.form['add']=='logout':
            return redirect('/login/')
    return render_template('reply.html',k=k,b=b,pf=pf,fo=fo,c=c,z=z)



