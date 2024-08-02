from pickle import dump,load
for i in range(0,12):
    i+=1
    iad='C:/Users/Toshiba/Desktop/Python files class 12/Python Project/Months/'+str(i)
    for j in range(0,31):
        j+=1
        jad=iad+'/'+str(j)+'.txt'
        myfile=open(jad,'ab+')
        List=[]
        for i in range(0,19):
            dump(List,myfile)
        myfile.seek(0)
        myfile.close()

'''
myfile=open('checkfile.txt','ab+')
List=[]
for i in range(1,20):
    dump(List,myfile)
myfile.seek(0)
try:
    while True:
        print(load(myfile))
except:
    myfile.close()
cn=int(input('Enter the list you want to input data in:-'))
myfile=open('checkfile.txt','ab+')
myfile.seek(0)
for i in range(1,cn+1):
    print(i,cn)
    if i==cn:
        print('hi')
        a=load(myfile)
        print(a)
        x=len(a)
        print(x)
        al=['hi','hello',98]
        print(al)
        a.append(al)
        print(a)'''

