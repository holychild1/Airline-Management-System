#Airlines root window

from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from pickle import load,dump
from tkcalendar import *
import datetime
from requests import get
from os import remove,rename

'''STAFF SPECIFIC INFORMATION'''
  
#All menu buttons of the module    
def menu_lp2():
    tableframe2.destroy()
    opt4.destroy()
    menulp2.destroy()
    option_page()

def menu_lp1():
    spframe.destroy()
    opt3.destroy()
    menulp.destroy()
    option_page()
    
def menu_opt3():
    tableframe1.destroy()
    opt2.destroy()
    menul3.destroy()
    option_page()
    
def menu_opt2():
    opt.destroy()
    sframe.destroy()
    menul2.destroy()
    option_page()
    
def menu_opt1():
    bframe.destroy()
    menul.destroy()
    option_page()

#Design and function of all passenger button
def OPT4():
    tableframe2.destroy()
    opt4.destroy()
    menulp2.destroy()
    category()
def ap_listex():
    global tableframe2,menulp2,opt4
    spframe.destroy()
    menulp.destroy()
    opt3.destroy()
    clnop={'CANBERRA,AUSTRALIA':0,
        'TORONTO,CANADA':1,
        'MONTREAL,CANADA':2,
        'PARIS,FRANCE':3,
        'BERLIN,GERMANY':4,
        'ATHENS,GREECE':5,
        'JAKARTA,INDONESIA':6,
        'ROME,ITALY':7,
        'MAURITIUS':8,
        'AMSTERDAM,NETHERLANDS':9,
        'MOSCOW,RUSSIA':10,
        'BARCELONA,SPAIN':11,
        'STOCKHOLM,SWEDEN':12,
        'ZURICH,SWITZERLAND':13,
        'ENGLAND,UK':14,
        'IRELAND,UK':15,
        'CALIFORNIA,USA':16,
        'NEW YORK,USA':17,
        'WASHINGTON,USA':18}
    tableframe2=Frame(root)
    tableframe2.pack(pady=10)
    scroll=Scrollbar(tableframe2)
    scroll.pack(side='right',fill=Y)
    table1=ttk.Treeview(tableframe2,yscrollcommand=scroll.set,selectmode='extended')
    table1.pack(fill='x',expand='yes')
    scroll.config(command=table1.yview)
    table1['columns']=('Flight No.','Passenger name','Mobile No.','Destination\
','Dep.Time','Arr.Time','Aisle/Window','Ec/Biz.')
    table1.column('#0',width=0,stretch='No')
    table1.column('Flight No.',anchor=W,width=120)
    table1.column('Passenger name',anchor=W,width=120)
    table1.column('Mobile No.',anchor=W,width=120)
    table1.column('Destination',anchor=W,width=120)
    table1.column('Dep.Time',anchor=W,width=120)
    table1.column('Arr.Time',anchor=W,width=120)
    table1.column('Aisle/Window',anchor=W,width=120)
    table1.column('Ec/Biz.',anchor=W,width=120)
    table1.heading('#0',text='',anchor=W)
    table1.heading('Flight No.',text='Flight No.',anchor=W)
    table1.heading('Passenger name',text='Passenger name',anchor=W)
    table1.heading('Mobile No.',text='Mobile No.',anchor=W)
    table1.heading('Destination',text='Destination',anchor=W)
    table1.heading('Dep.Time',text='Dep.Time',anchor=W)
    table1.heading('Arr.Time',text='Arr.Time',anchor=W)
    table1.heading('Aisle/Window',text='Aisle/Window',anchor=W)
    table1.heading('Ec/Biz.',text='Ec/Biz.',anchor=W)    
    cdt=Calp.get_date()
    cntry=p.get()
    myfile=open('Finfo.txt','rb')
    a=load(myfile)
    myfile.close()
    for i in a:
        if i[1]==cntry:
            cntin=i
    cdtf=cdt.split('/')
    pth='C:/Users/Toshiba/Desktop/Python files class 12/Python Project/Months/'+str(cdtf[0])+'/'+str(cdtf[1])+'.txt'
    myfile=open(pth,'rb')
    masterl=[]
    rfv=clnop[cntry]
    for i in range(0,rfv+1):
        c=load(myfile)
        if i==rfv:
            for j in c:
                tel=[]
                tel.append(cntin[0])
                tel.append(j[0])
                tel.append(j[1])
                tel.append(cntin[1])
                tel.append(cntin[5])
                tel.append(cntin[6])
                tel.append(j[4])
                tel.append(j[5])
                masterl.append(tel)
    x=5000
    for i in masterl:
        table1.insert(parent='',index='end',iid=x,text='',values=i)
        x+=1
    menulp2=Button(root,text='MENU',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=menu_lp2)
    menulp2.pack(side='bottom')
    opt4=Button(root,text='OPTIONS',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=OPT4)
    opt4.pack(side='bottom')  


def OPT3():
    spframe.destroy()
    menulp.destroy()
    opt3.destroy()
    category()    
def ap_list():
    menul.destroy()
    bframe.destroy()
    global spframe,menulp,Calp,p,opt3
    spframe=Frame(root,bg='lavender blush')
    spframe.pack()
    pe=Label(spframe,text='Destination -',bg='lavender blush',font=('Arial',20,'bold'))
    pe.grid(row=0,column=0)
    spe=Label(spframe,text='            ',bg='lavender blush',font=('Arial',20,'bold'))
    spe.grid(row=0,column=1)
    p=StringVar()
    p.set('CANBERRA,AUSTRALIA')
    xlist=[
        'CANBERRA,AUSTRALIA',
        'TORONTO,CANADA',
        'MONTREAL,CANADA',
        'PARIS,FRANCE',
        'BERLIN,GERMANY',
        'ATHENS,GREECE',
        'JAKARTA,INDONESIA',
        'ROME,ITALY',
        'MAURITIUS',
        'AMSTERDAM,NETHERLANDS',
        'MOSCOW,RUSSIA',
        'BARCELONA,SPAIN',
        'STOCKHOLM,SWEDEN',
        'ZURICH,SWITZERLAND',
        'ENGLAND,UK',
        'IRELAND,UK',
        'CALIFORNIA,USA',
        'NEW YORK,USA',
        'WASHINGTON,USA']
    p_entry=OptionMenu(spframe,p,*xlist)
    p_entry.grid(row=0,column=2)
    slabe=Label(spframe,text='       ',bg='lavender blush')
    slabe.grid(row=0,column=3)
    Date=Label(spframe,text='Date -',bg='lavender blush',font=('Arial',20,'bold'))
    Date.grid(row=0,column=4)
    Calp=Calendar(spframe,selectmode='day',year=2022,month=1,day=1)
    Calp.grid(row=0,column=5)
    Srbut=Button(spframe,text='Search',bg='light coral',width=12,height=1,font=('Arial',20,'bold'),command=ap_listex)
    Srbut.grid(row=1,column=0)
    menulp=Button(root,text='MENU',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=menu_lp1)
    menulp.pack(side='bottom')
    opt3=Button(root,text='OPTIONS',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=OPT3)
    opt3.pack(side='bottom')

#Design and function of passenger finder button    
def OPT2():
    tableframe1.destroy()
    menul3.destroy()
    opt2.destroy()
    category()
    
def pfinderex():
    global menul3,opt2,tableframe1
    menul2.destroy()
    opt.destroy()
    menul3=Button(root,text='MENU',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=menu_opt3)
    menul3.pack(side='bottom')
    opt2=Button(root,text='OPTIONS',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=OPT2)
    opt2.pack(side='bottom')
    Namef=NameE.get()
    Datef=Cal.get_date()
    sframe.destroy()
    clno={0:'CANBERRA,AUSTRALIA',
        1:'TORONTO,CANADA',
        2:'MONTREAL,CANADA',
        3:'PARIS,FRANCE',
        4:'BERLIN,GERMANY',
        5:'ATHENS,GREECE',
        6:'JAKARTA,INDONESIA',
        7:'ROME,ITALY',
        8:'MAURITIUS',
        9:'AMSTERDAM,NETHERLANDS',
        10:'MOSCOW,RUSSIA',
        11:'BARCELONA,SPAIN',
        12:'STOCKHOLM,SWEDEN',
        13:'ZURICH,SWITZERLAND',
        14:'ENGLAND,UK',
        15:'IRELAND,UK',
        16:'CALIFORNIA,USA',
        17:'NEW YORK,USA',
        18:'WASHINGTON,USA'}
    if Namef:
        tableframe1=Frame(root)
        tableframe1.pack(pady=10)
        scroll=Scrollbar(tableframe1)
        scroll.pack(side='right',fill=Y)
        table=ttk.Treeview(tableframe1,yscrollcommand=scroll.set,selectmode='extended')
        table.pack(fill='x',expand='yes')
        scroll.config(command=table.yview)
        table['columns']=('Flight No.','Passenger name','Mobile No.','Destination\
','Dep.Time','Arr.Time','Aisle/Window','Ec/Biz.')
        table.column('#0',width=0,stretch='No')
        table.column('Flight No.',anchor=W,width=120)
        table.column('Passenger name',anchor=W,width=120)
        table.column('Mobile No.',anchor=W,width=120)
        table.column('Destination',anchor=W,width=120)
        table.column('Dep.Time',anchor=W,width=120)
        table.column('Arr.Time',anchor=W,width=120)
        table.column('Aisle/Window',anchor=W,width=120)
        table.column('Ec/Biz.',anchor=W,width=120)
        table.heading('#0',text='',anchor=W)
        table.heading('Flight No.',text='Flight No.',anchor=W)
        table.heading('Passenger name',text='Passenger name',anchor=W)
        table.heading('Mobile No.',text='Mobile No.',anchor=W)
        table.heading('Destination',text='Destination',anchor=W)
        table.heading('Dep.Time',text='Dep.Time',anchor=W)
        table.heading('Arr.Time',text='Arr.Time',anchor=W)
        table.heading('Aisle/Window',text='Aisle/Window',anchor=W)
        table.heading('Ec/Biz.',text='Ec/Biz.',anchor=W)
        Datef=Datef.split('/')
        pth='C:/Users/Toshiba/Desktop/Python files class 12/Python Project/MONTHS/'+str(Datef[0])+'/'+str(Datef[1])+'.txt'
        myfile=open(pth,'rb')
        myfile2=open('Finfo.txt','rb')
        try:
            cl=[]
            cn=0
            rl=[]
            while True:
                a=load(myfile)
                x=len(a)
                if x!=0:
                    for i in a:
                        if i[0].lower()==Namef.lower():
                            det=[]
                            cl.append(cn)
                            det.append(i[0])
                            det.append(i[1])
                            det.append(i[4])
                            det.append(i[5])
                            rl.append(det)
                cn+=1
        except:
            myfile.close()
            cnt=[]
            for i in cl:
                cnt.append(clno[i])
            a=load(myfile2)
            clf=[]
            for i in cnt:
                cli=[]
                for j in a:
                    if j[1]==i:
                        cli.append(j[0])
                        cli.append(j[1])
                        cli.append(j[5])
                        cli.append(j[6])
                        clf.append(cli)
            fl=[]
            for i in range(0,len(rl)):
                il=[]
                il.append(clf[i][0])
                il.append(rl[i][0])
                il.append(rl[i][1])
                il.append(clf[i][1])
                il.append(clf[i][2])
                il.append(clf[i][3])
                il.append(rl[i][2])
                il.append(rl[i][3])
                fl.append(il)
            x=1000
            for i in fl:
                table.insert(parent='',index='end',iid=x,text='',values=i)
                x+=1
        else:
            messagebox.showerror('Error','Name not found')
            menul3.destroy()
            tableframe1.destroy()
            opt2.destroy()
            pfinder()
            myfile2.close()
    else:
        messagebox.showerror('Error','Please Enter a name')
        menul3.destroy()
        tableframe1.destroy()
        opt2.destroy()
        pfinder()
def OPT():
    sframe.destroy()
    menul2.destroy()
    opt.destroy()
    category()
    
def pfinder():
    menul.destroy()
    bframe.destroy()
    global sframe,NameE,Cal,menul2,opt
    sframe=Frame(root,bg='lavender blush')
    sframe.pack()
    NameL=Label(sframe,text='Name of passenger -',bg='lavender blush',font=('Arial',20,'bold'))
    NameL.grid(row=0,column=0)
    NameE=Entry(sframe,font=('Arial',16))
    NameE.grid(row=0,column=1)
    slabe=Label(sframe,text='       ',bg='lavender blush')
    slabe.grid(row=0,column=2)
    Date=Label(sframe,text='Date -',bg='lavender blush',font=('Arial',20,'bold'))
    Date.grid(row=0,column=3)
    Cal=Calendar(sframe,selectmode='day',year=2022,month=1,day=1)
    Cal.grid(row=0,column=4)
    Sbut=Button(sframe,text='Search',bg='light coral',width=12,height=1,font=('Arial',20,'bold'),command=pfinderex)
    Sbut.grid(row=1,column=0)
    menul2=Button(root,text='MENU',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=menu_opt2)
    menul2.pack(side='bottom')
    opt=Button(root,text='OPTIONS',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=OPT)
    opt.pack(side='bottom')

#Designing the home page of module
def category():
    logframe.destroy()
    menub.destroy()
    global bframe,menul
    bframe=Frame(root)
    bframe.pack()
    apb=Button(bframe,text='All Passengers',bg='light coral',width=32,height=4,font=('Arial',16,'bold'),command=ap_list)
    apb.pack()
    pfindb=Button(bframe,text='Passenger Search',bg='light coral',width=32,height=4,font=('Arial',16,'bold'),command=pfinder)
    pfindb.pack()
    menul=Button(root,text='MENU',bg='light coral',width=8,height=1,font=('Arial',16,'bold'),command=menu_opt1)
    menul.pack(side='bottom')
    
#Design and function of the login staff page    
def menu_login():
    logframe.destroy()
    menub.destroy()
    option_page()
    
def logcheck():
    try:
        ud=uid.get()
        pd=pwd.get()
        logframe.destroy()
        myfile=open('C:/Users/Toshiba/Desktop/Python files class 12/Python Project/Python password module/Private/linfo.dat','rb')
        data=load(myfile)
        myfile.close()
        x=0
        for i in data:
            if ud==i[0] and pd==i[1]:
                x=1
        if x==0:
            messagebox.showerror('Error','Your login credentials are incorrect')
            menub.destroy()
            pipinfo()
        elif x==1:
            category()
    except FileNotFoundError:
        messagebox.showerror('Error','Authenticate the file by unlocking the ID info folder')
        menub.destroy()
        option_page()
    
def pipinfo():
    global logframe,uid,pwd,menub
    pinfo.destroy()
    finfo.destroy()
    winfo.destroy()
    root.configure(bg='lavender blush')
    logframe=LabelFrame(root,text='LOGIN',background='maroon',fg='white',font=('Arial',20,'bold'))
    logframe.place(relx=0.5,rely=0.5,anchor='center')
    u=Label(logframe,text='User ID:-',background='maroon',fg='white',font=('Arial',20,'bold'))
    u.grid(row=0,column=0,padx=10,pady=10)
    uid=Entry(logframe,font=('Arial',18))
    uid.grid(row=0,column=1,padx=10,pady=10)
    p=Label(logframe,text='Password:-',fg='white',background='maroon',font=('Arial',20,'bold'))
    p.grid(row=1,column=0,padx=10,pady=10)
    pwd=Entry(logframe,show='*',font=('Arial',18))
    pwd.grid(row=1,column=1,padx=10,pady=10)
    logb=Button(logframe,text='LOGIN',bg='lavender blush',width=14,height=1,font=('Arial',16,'bold'),command=logcheck)
    logb.grid(row=2,column=3,padx=10,pady=10)
    menub=Button(root,text='MENU',bg='violet',width=8,height=1,font=('Arial',16,'bold'),command=menu_login)
    menub.pack(side='bottom')

'''WEATHER PAGE'''

#Displaying the info
def menu_wtr():
    locate.destroy()
    lcation.destroy()
    label.destroy()
    temp.destroy()
    weatherl.destroy()
    desc.destroy()
    menuw2.destroy()
    option_page()

def display_weather():
    menuw.destroy()
    global locate,lcation,label,temp,weatherl,desc,menuw2
    root.configure(bg='mistyrose2')
    locate=Label(root,text='LOCATION:-',background='mistyrose2',font=('Arial',18))
    locate.pack()
    lcation=Label(root,text='{},{}'.format(final[0],final[1]),background='mistyrose2',font=('Arial',18))
    lcation.pack()
    img=ImageTk.PhotoImage(Image.open(final[5]+'.jpg'))
    label=Label(image=img,background='mistyrose2')
    label.image=img
    label.pack()
    temp=Label(root,text='{}K, {:.2f}°C, {:.2f}°F'.format(final[2],final[3],final[4]),background='mistyrose2',font=('Arial',18))
    temp.pack()
    weatherl=Label(root,text=final[6],background='mistyrose2',font=('Arial',18))
    weatherl.pack()
    desc=Label(root,text=final[7],background='mistyrose2',font=('Arial',18))
    desc.pack()
    menuw2=Button(root,text='MENU',bg='violet',width=8,height=1,font=('Arial',16,'bold'),command=menu_wtr)
    menuw2.pack(side='bottom')

#Designing GUI components
def menu_wthr():
    frm.destroy()
    menuw.destroy()
    option_page()
    
def site():
    global frm,cit,menuw
    finfo.destroy()
    winfo.destroy()
    pinfo.destroy()
    frm=Frame(root,background='indianred')
    frm.pack()
    si=Label(frm,text='Enter Name of city:-',background='indianred',font=('Arial',18))
    si.pack()
    cit=Entry(frm,font=('Arial',18))
    cit.pack()
    sb=Button(frm,text='Search',bg='violet',width=14,height=1,font=('Arial',16,'bold'),command=weather)
    sb.pack()
    menuw=Button(root,text='MENU',bg='violet',width=8,height=1,font=('Arial',16,'bold'),command=menu_wthr)
    menuw.pack(side='bottom')

#Getting info from external api    
def weather():
    global frm,cit,final
    cityg=cit.get()
    frm.destroy()
    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    req=get(url.format(cityg,'03af6030b96842bc7dce9a6285766353'))
    if req:
        json=req.json()
        city=json['name']
        country=json['sys']['country']
        tempk=json['main']['temp']
        tempc=tempk-273.5
        tempf=(tempk-273.5)*9/5+32
        icon=json['weather'][0]['icon']
        weather=json['weather'][0]['main']
        weatherd=json['weather'][0]['description']
        final=(city,country,tempk,tempc,tempf,icon,weather,weatherd)
        display_weather()
    else:
        messagebox.showerror('Error','Can not find the city {}'.format(cityg))
        option_page()


'''BOOKING FUNCTION'''

#Designing the ticket
def menu_T():
    root1.destroy()
    menuT.destroy()
    option_page()
    
def ticket():
    menub.destroy()
    global root1,menuT
    myfile=open('Finfo.txt','rb')
    a=load(myfile)
    myfile.close()
    for i in a:
        if i[1]==tget:
            x=i
    plist=[pname,pphone,x[0],x[1],x[2],x[7],x[5],x[6],tseat,pseat]
    root1=LabelFrame(root,text='TICKET:-',bg='mistyrose2',font=('Arial',20,'bold'))
    root1.pack()
#   Name display
    nmr=Frame(root1,bg='indianred')
    nmr.grid(row=0,column=0,padx=10,pady=10)
    nm=Label(nmr,text='NAME-',background='mistyrose2',font=('Arial',18))
    nm.grid(row=0,column=0,padx=10,pady=10)
    to1=Label(nmr,text=plist[0],background='mistyrose2',font=('Arial',18))
    to1.grid(row=0,column=1,padx=10,pady=10)
#   Phone number display
    phr=Frame(root1,bg='indianred')
    phr.grid(row=0,column=1,padx=10,pady=10)
    ph=Label(phr,text='PHONE NO.-',background='mistyrose2',font=('Arial',18))
    ph.grid(row=0,column=0,padx=10,pady=10)
    to2=Label(phr,text=plist[1],background='mistyrose2',font=('Arial',18))
    to2.grid(row=0,column=1,padx=10,pady=10)
#   Flight No. display
    fnr=Frame(root1,bg='indianred')
    fnr.grid(row=0,column=2,padx=10,pady=10)    
    fn=Label(fnr,text='FLIGHT NO.-',background='mistyrose2',font=('Arial',18))
    fn.grid(row=0,column=0,padx=10,pady=10)
    to3=Label(fnr,text=plist[2],background='mistyrose2',font=('Arial',18))
    to3.grid(row=0,column=5,padx=10,pady=10)
#   Destination Display
    frr=Frame(root1,bg='indianred')
    frr.grid(row=1,column=0,padx=10,pady=10)
    fr=Label(frr,text='DESTINATION-',background='mistyrose2',font=('Arial',18))
    fr.grid(row=0,column=0,padx=10,pady=10)
    to4=Label(frr,text=plist[3],background='mistyrose2',font=('Arial',18))
    to4.grid(row=0,column=1,padx=10,pady=10)
#   From display
    der=Frame(root1,bg='indianred')
    der.grid(row=1,column=1,padx=10,pady=10)
    des=Label(der,text='FROM-',background='mistyrose2',font=('Arial',18))
    des.grid(row=0,column=0,padx=10,pady=10)
    to5=Label(der,text=plist[4],background='mistyrose2',font=('Arial',18))
    to5.grid(row=0,column=1,padx=10,pady=10)
#   Gate no. display
    gtr=Frame(root1,bg='indianred')
    gtr.grid(row=1,column=2,padx=10,pady=10)
    gt=Label(gtr,text='GATE NO.-',background='mistyrose2',font=('Arial',18))
    gt.grid(row=0,column=0,padx=10,pady=10)
    to6=Label(gtr,text=plist[5],background='mistyrose2',font=('Arial',18))
    to6.grid(row=0,column=1,padx=10,pady=10)
#   Departure time display
    dpr=Frame(root1,bg='indianred')
    dpr.grid(row=2,column=0,padx=10,pady=10)
    dep=Label(dpr,text='DEPARTURE-',background='mistyrose2',font=('Arial',18))
    dep.grid(row=0,column=0,padx=10,pady=10)
    to7=Label(dpr,text=plist[6],background='mistyrose2',font=('Arial',18))
    to7.grid(row=0,column=1,padx=10,pady=10)
#   Arrival time display
    arr=Frame(root1,bg='indianred')
    arr.grid(row=2,column=1,padx=10,pady=10)
    ar=Label(arr,text='ARRIVAL-',background='mistyrose2',font=('Arial',18))
    ar.grid(row=0,column=0,padx=10,pady=10)
    to8=Label(arr,text=plist[7],background='mistyrose2',font=('Arial',18))
    to8.grid(row=0,column=1,padx=10,pady=10)
#   Type of seat display
    tsr=Frame(root1,bg='indianred')
    tsr.grid(row=2,column=2,padx=10,pady=10)
    tos=Label(tsr,text='TYPE OF SEAT-',background='mistyrose2',font=('Arial',18))
    tos.grid(row=0,column=0,padx=10,pady=10)
    to9=Label(tsr,text=plist[8],background='mistyrose2',font=('Arial',18))
    to9.grid(row=0,column=1,padx=10,pady=10)
#   Class Display
    csr=Frame(root1,bg='indianred')
    csr.grid(row=3,column=0,padx=10,pady=10)
    cls=Label(csr,text='CLASS-',background='mistyrose2',font=('Arial',18))
    cls.grid(row=0,column=0,padx=10,pady=10)
    to10=Label(csr,text=plist[9],background='mistyrose2',font=('Arial',18))
    to10.grid(row=0,column=1,padx=10,pady=10)
    menuT=Button(root,text='MENU',bg='violet',width=8,height=1,font=('Arial',16,'bold'),command=menu_T)
    menuT.pack(side='bottom')  

#Entering the data in files
def data_entry():
    clno={'CANBERRA,AUSTRALIA':0,
        'TORONTO,CANADA':1,
        'MONTREAL,CANADA':2,
        'PARIS,FRANCE':3,
        'BERLIN,GERMANY':4,
        'ATHENS,GREECE':5,
        'JAKARTA,INDONESIA':6,
        'ROME,ITALY':7,
        'MAURITIUS':8,
        'AMSTERDAM,NETHERLANDS':9,
        'MOSCOW,RUSSIA':10,
        'BARCELONA,SPAIN':11,
        'STOCKHOLM,SWEDEN':12,
        'ZURICH,SWITZERLAND':13,
        'ENGLAND,UK':14,
        'IRELAND,UK':15,
        'CALIFORNIA,USA':16,
        'NEW YORK,USA':17,
        'WASHINGTON,USA':18}
    ino=clno[tget]
    date1=date.split('/')
    pth='C:/Users/Toshiba/Desktop/Python files class 12/Python Project/Months/'+str(date1[0])+'/'+str(date1[1])+'.txt'
    myfile=open(pth,'rb')
    pth2='C:/Users/Toshiba/Desktop/Python files class 12/Python Project/Months/'+str(date1[0])+'/test.txt'
    myfile2=open(pth2,'wb')
    detail=[pname,pphone,nseats,date,pseat,tseat]
    myfile.seek(0)
    for i in range(0,ino+1):
        a=load(myfile)
        if i==ino:
            a.append(detail)
        dump(a,myfile2)
    for i in range(ino+1,19):
        a=load(myfile)
        dump(a,myfile2)
    myfile.close()
    myfile2.close()
    remove(pth)
    rename(pth2,pth)
    ticket()
    
#Getting info from GUI componentss
def booking():
    global tframe,dataframe,pname,pphone,nseats,date,pseat,tseat
    global name,name_en,phone,phone_en,num,fdigit,sdigit,cal,dat,date
    global fdigi,sdigi,stype,cstype,stype_entry,seat,seat_entry,book,clicked
    pname=name_en.get()
    pphone=phone_en.get()
    nseats=fdigi.get()+sdigi.get()
    date=cal.get_date()
    pseat=cstype.get()
    tseat=clicked.get()
    if pname and pphone:
        if len(str(pphone))==10:
            s=int(pphone)
            tframe.destroy()
            dataframe.destroy()
            data_entry()
    if len(str(pphone))!=10:
        messagebox.showerror('Error','Invalid Phone Number.')
    if not pname:
        messagebox.showerror('Error','Please fill in your name.')
    elif not pphone:
        messagebox.showerror('Error','Please fill in your phone number.')
   
    
def menu_book():
    menub.destroy()
    tframe.destroy()
    dataframe.destroy()
    option_page()
  
    
#Designing the GUI components    
def search():
    global t,tframe,dataframe,menub,tget
    tget=t.get()
    toframe.destroy()
    tableframe.destroy()
    myfile=open('Finfo.txt','rb')
    data=load(myfile)
    tframe=Frame(root)
    tframe.pack()
    ttable=ttk.Treeview(tframe)
    ttable.pack(fill='x',expand='y')
    ttable['columns']=('Flight No.','To','From','Fare(ec)','Fare(biz.)','Dep.Time\
','Arr.Time','Gate','Seats(w)','Seats(a)','Seats(biz.)')
    ttable.column('#0',width=0,stretch='No')
    ttable.column('Flight No.',anchor=W,width=120)
    ttable.column('To',anchor=W,width=120)
    ttable.column('From',anchor=W,width=120)
    ttable.column('Fare(ec)',anchor=W,width=120)
    ttable.column('Fare(biz.)',anchor=W,width=120)
    ttable.column('Dep.Time',anchor=W,width=120)
    ttable.column('Arr.Time',anchor=W,width=120)
    ttable.column('Gate',anchor=W,width=120)
    ttable.column('Seats(w)',anchor=W,width=120)
    ttable.column('Seats(a)',anchor=W,width=120)
    ttable.column('Seats(biz.)',anchor=W,width=120)
    ttable.heading('#0',text='',anchor=W)
    ttable.heading('Flight No.',text='Flight No.',anchor=W)
    ttable.heading('To',text='TO',anchor=W)
    ttable.heading('From',text='FROM',anchor=W)
    ttable.heading('Fare(ec)',text='Fare(ec)',anchor=W)
    ttable.heading('Fare(biz.)',text='Fare(biz.)',anchor=W)
    ttable.heading('Dep.Time',text='Dep.Time',anchor=W)
    ttable.heading('Arr.Time',text='Arr.Time',anchor=W)
    ttable.heading('Gate',text='Gate',anchor=W)
    ttable.heading('Seats(w)',text='Seats(w)',anchor=W)
    ttable.heading('Seats(a)',text='Seats(a)',anchor=W)
    ttable.heading('Seats(biz.)',text='Seats(biz.)',anchor=W)
    x=100
    for i in data:
        if tget.lower()==i[1].lower():
            ttable.insert(parent='',index='end',iid=x,text='',values=i)
            x+=1
    global name,name_en,phone,phone_en,num,fdigit,sdigit,cal,dat
    global fdigi,sdigi,stype,cstype,stype_entry,seat,seat_entry,book,clicked
    dataframe=LabelFrame(root,text='BOOKING DETAILS',background='indianred',font=('Arial',20,'bold'))
    dataframe.pack(fill='x')
    name=Label(dataframe,text='Name:-',background='indianred',font=('Arial',18))
    name.grid(row=0,column=0,padx=10,pady=10)
    name_en=Entry(dataframe,font=('Arial',18))
    name_en.grid(row=0,column=1,padx=10,pady=10)
    phone=Label(dataframe,text='Mobile No.:-',background='indianred',font=('Arial',18))
    phone.grid(row=0,column=2,padx=10,pady=10)
    phone_en=Entry(dataframe,font=('Arial',18))
    phone_en.grid(row=0,column=3,padx=10,pady=10)    
    num=Label(dataframe,text='Number of seats:-',background='indianred',font=('Arial',18))
    num.grid(row=0,column=4,padx=10,pady=10)
    fdigi=StringVar()
    fdigi.set(0)
    flist=['0','1','2','3','4','5','6','7','8','9']
    fdigit=OptionMenu(dataframe,fdigi,*flist)
    fdigit.grid(row=0,column=5)
    sdigi=StringVar()
    sdigi.set(1)
    sdigit=OptionMenu(dataframe,sdigi,*flist)
    sdigit.grid(row=0,column=6)
    dat=Label(dataframe,text='Date:-',background='indianred',font=('Arial',18))
    dat.grid(row=1,column=0,padx=10,pady=10)
    cal=Calendar(dataframe,selectmode='day',year=2022,month=1,day=1)
    cal.grid(row=1,column=1)
    stype=Label(dataframe,text='Seat Type:-',background='indianred',font=('Arial',18))
    stype.grid(row=1,column=2,padx=10,pady=10)
    cstype=StringVar()
    cstype.set('Economy')
    stype_entry=OptionMenu(dataframe,cstype,'Economy','Business Class')
    stype_entry.grid(row=1,column=3,padx=10,pady=10)    
    seat=Label(dataframe,text='Preferred Seat:-',background='indianred',font=('Arial',18))
    seat.grid(row=1,column=4,padx=10,pady=10)
    clicked=StringVar()
    clicked.set('Aisle')
    seat_entry=OptionMenu(dataframe,clicked,'Aisle','Window')
    seat_entry.grid(row=1,column=5,padx=10,pady=10)
    book=Button(dataframe,text='BOOK',bg='violet',width=14,height=1,font=('Arial',16,'bold'),command=booking)
    book.grid(row=6,column=0,padx=10,pady=10)
    confirm=Button(dataframe,text='BOOK',bg='violet',width=14,height=1,font=('Arial',16,'bold'),command=booking)
    confirm.grid(row=6,column=0,padx=10,pady=10)
    menub=Button(root,text='MENU',bg='violet',width=8,height=1,font=('Arial',16,'bold'),command=menu_book)
    menub.pack(side='bottom')
        

def tofrom():
    global toframe
    toframe=LabelFrame(root,text='DESTINATION',background='indianred',font=('Arial',20,'bold'))
    toframe.pack(fill='x',pady=20)
    to=Label(toframe,text='To:-',background='indianred',font=('Arial',18))
    to.grid(row=0,column=0,padx=10,pady=10)
    global t
    t=StringVar()
    t.set('CANBERRA,AUSTRALIA')
    xlist=[
        'CANBERRA,AUSTRALIA',
        'TORONTO,CANADA',
        'MONTREAL,CANADA',
        'PARIS,FRANCE',
        'BERLIN,GERMANY',
        'ATHENS,GREECE',
        'JAKARTA,INDONESIA',
        'ROME,ITALY',
        'MAURITIUS',
        'AMSTERDAM,NETHERLANDS',
        'MOSCOW,RUSSIA',
        'BARCELONA,SPAIN',
        'STOCKHOLM,SWEDEN',
        'ZURICH,SWITZERLAND',
        'ENGLAND,UK',
        'IRELAND,UK',
        'CALIFORNIA,USA',
        'NEW YORK,USA',
        'WASHINGTON,USA']
    t_entry=OptionMenu(toframe,t,*xlist)
    t_entry.grid(row=0,column=1,padx=10,pady=10)
    searchb=Button(toframe,text='SEARCH',bg='violet',width=14,height=1,font=('Arial',16,'bold'),command=search)
    searchb.grid(row=1,column=6,padx=10,pady=10)
#Designing Treeview    
def flight_table():
    finfo.destroy()
    winfo.destroy()
    pinfo.destroy()
    global tableframe
    tableframe=Frame(root)
    tableframe.pack(pady=10)
    scroll=Scrollbar(tableframe)
    scroll.pack(side='right',fill=Y)
    table=ttk.Treeview(tableframe,yscrollcommand=scroll.set,selectmode='extended')
    table.pack(fill='x',expand='yes')
    scroll.config(command=table.yview)
    table['columns']=('Flight No.','To','From','Fare(ec)','Fare(biz.)','Dep.Time\
','Arr.Time','Gate','Seats(w)','Seats(a)','Seats(biz.)')
    table.column('#0',width=0,stretch='No')
    table.column('Flight No.',anchor=W,width=120)
    table.column('To',anchor=W,width=120)
    table.column('From',anchor=W,width=120)
    table.column('Fare(ec)',anchor=W,width=120)
    table.column('Fare(biz.)',anchor=W,width=120)
    table.column('Dep.Time',anchor=W,width=120)
    table.column('Arr.Time',anchor=W,width=120)
    table.column('Gate',anchor=W,width=120)
    table.column('Seats(w)',anchor=W,width=120)
    table.column('Seats(a)',anchor=W,width=120)
    table.column('Seats(biz.)',anchor=W,width=120)
    table.heading('#0',text='',anchor=W)
    table.heading('Flight No.',text='Flight No.',anchor=W)
    table.heading('To',text='TO',anchor=W)
    table.heading('From',text='FROM',anchor=W)
    table.heading('Fare(ec)',text='Fare(ec)',anchor=W)
    table.heading('Fare(biz.)',text='Fare(biz.)',anchor=W)
    table.heading('Dep.Time',text='Dep.Time',anchor=W)
    table.heading('Arr.Time',text='Arr.Time',anchor=W)
    table.heading('Gate',text='Gate',anchor=W)
    table.heading('Seats(w)',text='Seats(w)',anchor=W)
    table.heading('Seats(a)',text='Seats(a)',anchor=W)
    table.heading('Seats(biz.)',text='Seats(biz.)',anchor=W)
    myfile=open('Finfo.txt','rb')
    rec=load(myfile)
    n=0
    for i in rec:
        table.insert(parent='',index='end',iid=n,text='',values=i)
        n+=1
    myfile.close()
    tofrom()  

#Designing The Root Window   
    
def option_page():
    global l,finfo,winfo,pinfo
    l.destroy()
    root.configure(bg='indianred')
    finfo=Button(text='FLIGHT INFORMATION',bg='indianred',width=25,height=3,font=('Lato',18,'bold'),command=flight_table)
    finfo.pack()
    winfo=Button(text='WEATHER UPDATE',bg='indianred',width=25,height=3,font=('Lato',18,'bold'),command=site)
    winfo.pack()
    pinfo=Button(text='PASSENGER INFORMATION',bg='indianred',width=25,height=3,font=('Lato',18,'bold'),command=pipinfo)
    pinfo.pack()
root=Tk()
root.geometry('1920x1080')
root.state('zoomed')

root.title('The Airlines For You(TAFY)')
root.configure(bg='mistyrose2')
img=ImageTk.PhotoImage(Image.open('logo.png'))
l=Label(image=img)
l.pack()
l.after(5000,option_page)




