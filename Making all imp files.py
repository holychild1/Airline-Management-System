#Airlines all important files
from pickle import load,dump

myfile=open('Finfo.txt','ab')
n=myfile.tell()
if n==0:
    ir=['28IE15','IRELAND,UK','DELHI','60,000','1,65,333','19:00','4:30','3','40','40','20']
    en=['69EN11','ENGLAND,UK','DELHI','57,814','1,61,182','1:00','11:00','2','40','40','20']
    cl=['52CL89','CALIFORNIA,USA','DELHI','70,000','2,39,000','3:00','23:00','3','40','40','20']
    dc=['28DC66','WASHINGTON,USA','DELHI','59,000','2,29,000','18:00','10:00','1','40','40','20']
    ny=['76NY23','NEW YORK,USA','DELHI','59,000','2,31,000','5:00','2:00','1','40','40','20']
    c1=['83TR12','TORORNTO,CANADA','DELHI','70,136','2,59,040','7:00','20:00','2','40','40','20']
    c2=['43MN10','MONTREAL,CANADA','DELHI','70,136','2,59,040','16:00','5:00','2','40','40','20']
    fr=['62FR02','PARIS,FRANCE','DELHI','57,673','1,35,084','8:00','16:00','3','40','40','20']
    gr=['74GR37','BERLIN,GERMANY','DELHI','56,436','1,66,699','9:00','19:00','1','40','40','20']
    it=['92IT87','ROME,ITALY','DELHI','59,313','1,12,251','10:00','16:00','2','40','40','20']
    sp=['58SP29','BARCELONA,SPAIN','DELHI','54,004','1,30,158','11:00','23:00','3','40','40','20']
    au=['92AU09','CANBERRA,AUSTRALIA','DELHI','74,736','2,00,163','12:00','1:00','1','40','40','20']
    mr=['89MR42','MAURITIUS','DELHI','23,875','1,66,071','13:00','20:30','2','40','40','20']
    gc=['61GR27','ATHENS,GREECE','DELHI','66,536','1,87,769','14:00','2:30','3','40','40','20']
    mc=['56MC21','MOSCOW,RUSSIA','DELHI','48,508','1,62,927','2:30','8:50','1','40','40','20']
    Is=['35IS53','JAKARTA,INDONESIA','DELHI','13,974','88,430','16:00','1:00','1','40','40','20']
    sw=['15SW76','STOCKHOLM,SWEDEN','DELHI','55,266','1,52,372','17:00','5:00','2','40','40','20']
    nl=['54NL42','AMSTERDAM,NETHERLANDS','DELHI','60,076','1,48,883','17:30','1:00','3','40','40','20']
    sl=['35SL28','ZURICH,SWITZERLAND','DELHI','67,018','1,85,351','0:00','8:00','3','40','40','20']
    rec=[ir,en,cl,dc,ny,c1,c2,fr,gr,it,sp,au,mr,gc,mc,Is,sw,nl,sl]
    dump(rec,myfile)
myfile.close()
myfile=open('Finfo.txt','rb')
try:
    while True:
        print()
        i=load(myfile)
        for j in i:
            print()
            for k in j:
                print(k,end=' $ ')
except:
    myfile.close()

'''myfile=open('linfo.dat','wb')
idlist=[['PA2908AK','AK09AST'],['KA2811KA','KA04TCH'],['BH5687SA','SA58GHT']]
dump(idlist,myfile)
myfile.close()
myfile=open('C:/Users/Toshiba/Desktop/Python files class 12/Python Project/Python password module/Private/linfo.dat','rb')
print(load(myfile))
myfile.close()'''

