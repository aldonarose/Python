import mysql.connector
import datetime
mydb=mysql.connector.connect(host='localhost',user='root',password='aldo_365',database='jasvts')
mycursor=mydb.cursor(buffered = True)
print("              JASVTS VACCINATION TRACKING SYSTEM                ")
while True:
    print()
    print('1.INSERT RECORD')
    print('2.SEARCH RECORD')
    print('3.UPDATE RECORD')
    print('4.DELETE RECORD')
    print('ENTER 0 TO EXIT')
    print()
    ch=int(input('ENTER CHOICE: '))
    print()
    if ch==0:
        print('EXITING THE PROGRAM')
        break
    elif ch==1:
        print('''1.PRIOR APPOINTMENTS
2.VACCINES
3.PFIZER
4.MODERNA
5.COVAXIN \n''')
        ch1=int(input("ENTER CHOICE: "))
        print()
        if ch1==1:
            while True:
                regno=int(input('ENTER REGISTRATION NUMBER: '))
                name=input('ENTER FULLNAME: ')
                idno=int(input('ENTER EMIRATES ID NUMBER: '))
                vac=input('ENTER VACCINE NAME: ')
                date=input('ENTER DATE (YYYY-MM-DD): ')
                time=input('ENTER TIME (HH:MM:SS): ')
                mycursor.execute("INSERT INTO PRIORAPPOINTMENTS VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','"+vac+"','"+date+"','"+time+"')")
                mydb.commit()
                b=input("DO YOU WANT TO EXIT (Y/N): ")
                if b=='Y':
                    break
            mycursor.execute("SELECT* FROM PRIORAPPOINTMENTS")
            print("\nTHE FOLLOWING RECORDS HAVE BEEN SUCCESSFULLY INSERTED:\n")
            data=mycursor.fetchall()
            for i in data:
                for j in i:
                    print(j,end=" ")
                print()
            mydb.commit()
        elif ch1==2:
            while True:
                vac=input("ENTER THE VACCINE NAME: ")
                am=int(input("ENTER THE AMOUNT AVAILABLE: "))
                mycursor.execute("INSERT INTO VACCINES VALUES('"+vac+"','"+str(am)+"')")
                mydb.commit()
                b=input("DO YOU WANT TO EXIT (Y/N): ")
                if b=='Y':
                    break
            mycursor.execute("SELECT* FROM VACCINES")
            print("\nTHE FOLLOWING RECORDS HAVE BEEN SUCCESSFULLY INSERTED:\n")
            data=mycursor.fetchall()
            for i in data:
                for j in i:
                    print(j,end="  ")
                print()
            mydb.commit()
        elif ch1 in (3,4,5):
            while True:
                regno=int(input('ENTER REGISTRATION NUMBER: '))
                name=input('ENTER FULLNAME: ')
                idno=int(input('ENTER EMIRATES ID NUMBER: '))
                first=input('ENTER DATE OF FIRST DOSE (YYYY-MM-DD): ')
                f1=datetime.datetime.strptime(first,"%Y-%m-%d")
                status=input("ENTER STATUS: ")
                if ch1==3:
                    n=f1+datetime.timedelta(days=21)
                    second=str(n).rstrip(" 00:00:00")
                    mycursor.execute("INSERT INTO PFIZER (REGNO,FULLNAME,IDNO,FIRSTDOSE,SECONDDOSE,STATUS) VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','"+first+"','"+second+"','"+status+"')")
                    if status=='COMPLETED':
                        mycursor.execute("INSERT INTO COMPLETED VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','PFIZER','"+first+"','"+second+"')")   
                    mydb.commit()
                    mycursor.execute("SELECT* FROM PFIZER") 
                elif ch1==4:
                    n=f1+datetime.timedelta(days=28)
                    second=str(n).rstrip(" 00:00:00")
                    mycursor.execute("INSERT INTO MODERNA (REGNO,FULLNAME,IDNO,FIRSTDOSE,SECONDDOSE,STATUS) VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','"+first+"','"+second+"','"+status+"')")
                    if status=='COMPLETED':
                        mycursor.execute("INSERT INTO COMPLETED VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','MODERNA','"+first+"','"+second+"')")
                    mydb.commit()
                    mycursor.execute("SELECT* FROM MODERNA")
                elif ch1==5:
                    n=f1+datetime.timedelta(days=28)
                    second=str(n).rstrip(" 00:00:00")
                    mycursor.execute("INSERT INTO COVAXIN (REGNO,FULLNAME,IDNO,FIRSTDOSE,SECONDDOSE,STATUS) VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','"+first+"','"+second+"','"+status+"')")
                    if status=='COMPLETED':
                        mycursor.execute("INSERT INTO COMPLETED VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','COVAXIN','"+first+"','"+second+"')")
                    mydb.commit()
                    mycursor.execute("SELECT* FROM COVAXIN")
                b=input("DO YOU WANT TO EXIT (Y/N): ")
                if b=='Y':
                    break
            print("\nTHE FOLLOWING RECORDS HAVE BEEN SUCCESSFULLY INSERTED:\n")
            data=mycursor.fetchall()
            for i in data:
                for j in i:
                    print(j,end="  ")
                print()
            mydb.commit()
    elif ch==2:
        print('''1.PRIOR APPOINTMENTS
2.VACCINES
3.PFIZER
4.MODERNA
5.COVAXIN
6.COMPLETED VACCINATION\n''')
        ch1=int(input("ENTER CHOICE: "))
        print()
        if ch1==1:
            idno=int(input('ENTER EMIRATES ID NUMBER TO SEARCH FOR: '))
            mycursor.execute("SELECT * FROM PRIORAPPOINTMENTS WHERE IDNO=%s"%(idno,))
        elif ch1==2:
            vac=input('ENTER VACCINE NAME TO SEARCH FOR: ')
            mycursor.execute("SELECT * FROM VACCINES WHERE VACCINE=%s"%('"'+vac+'"',))
        elif ch1==3:
            idno=int(input('ENTER EMIRATES ID NUMBER TO SEARCH FOR: '))
            mycursor.execute("SELECT * FROM PFIZER WHERE IDNO=%s"%(idno,))
        elif ch1==4:
            idno=int(input('ENTER EMIRATES ID NUMBER TO SEARCH FOR: '))
            mycursor.execute("SELECT * FROM MODERNA WHERE IDNO=%s"%(idno,))
            
        elif ch1==5:
            idno=int(input('ENTER EMIRATES ID NUMBER TO SEARCH FOR: '))
            mycursor.execute("SELECT * FROM COVAXIN WHERE IDNO=%s"%(idno,))
           
        elif ch1==6:
            idno=int(input('ENTER EMIRATES ID NUMBER TO SEARCH FOR: '))
            mycursor.execute("SELECT * FROM COMPLETED WHERE IDNO=%s"%(idno,))
        
        data=mycursor.fetchall()
        if data==[]:
            print('RECORD NOT FOUND')
        else:
            print("\nTHE RECORD HAS BEEN FOUND:\n")
            for i in data:
                for j in i:
                    print(j,end="  ")
                print()
            mydb.commit()
    elif ch==3:
        print('''1.PRIOR APPOINTMENTS
2.VACCINES
3.PFIZER
4.MODERNA
5.COVAXIN\n''')
        ch3=int(input("ENTER THE TABLE TO UPDATE: "))
        print()
        if ch3==1:
            regno=int(input("ENTER REGISTRATION NUMBER: ")) 
            date=input("ENTER UPDATED DATE: ")
            mycursor.execute("UPDATE PRIORAPPOINTMENTS SET DATE=%s WHERE REGNO=%s"%('"'+date+'"',regno))
            mydb.commit()
            mycursor.execute("SELECT* FROM PRIORAPPOINTMENTS")
        elif ch3==2:
            vac=input("ENTER VACCINE: ") 
            amount=int(input("ENTER UPDATED AMOUNT: "))
            mycursor.execute("UPDATE VACCINES SET AMOUNT_AVAILABLE=%s WHERE VACCINE=%s"%(amount,'"'+vac+'"'))
            mydb.commit()
            mycursor.execute("SELECT* FROM VACCINES")
        elif ch3==3:
            regno=int(input("ENTER REGISTRATION NUMBER: ")) 
            status=input("ENTER UPDATED STATUS: ")
            mycursor.execute("UPDATE PFIZER SET STATUS=%s WHERE REGNO=%s"%('"'+status+'"',regno))
            mydb.commit()
            if status=='COMPLETED':
                        mycursor.execute("SELECT * FROM PFIZER WHERE REGNO=%s"%(regno,))
                        data=mycursor.fetchall()
                        for i in data:
                              RS=i
                        name,idno,first,second=RS[1],RS[2],RS[3],RS[4]
                        mydb.commit()
                        mycursor.execute("INSERT INTO COMPLETED VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','PFIZER','"+str(first)+"','"+str(second)+"')")
            mydb.commit()
            mycursor.execute("SELECT* FROM PFIZER")
        elif ch3==4:
            regno=int(input("ENTER REGISTRATION NUMBER: ")) 
            status=input("ENTER UPDATED STATUS : ")
            mycursor.execute("UPDATE MODERNA SET STATUS=%s WHERE REGNO=%s"%('"'+status+'"',regno))
            mydb.commit()
            if status=='COMPLETED':
                        mycursor.execute("SELECT * FROM MODERNA WHERE REGNO=%s"%(regno,))
                        data=mycursor.fetchall()
                        for i in data:
                              RS=i
                        name,idno,first,second=RS[1],RS[2],RS[3],RS[4]
                        mydb.commit()
                        mycursor.execute("INSERT INTO COMPLETED VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','MODERNA','"+str(first)+"','"+str(second)+"')")
            mydb.commit()
            mycursor.execute("SELECT* FROM MODERNA")
        elif ch3==5:
            regno=int(input("ENTER REGISTRATION NUMBER: ")) 
            status=input("ENTER UPDATED STATUS: ")
            mycursor.execute("UPDATE COVAXIN SET STATUS=%s WHERE REGNO=%s"%('"'+status+'"',regno))
            mydb.commit()
            if status=='COMPLETED':
                        mycursor.execute("SELECT * FROM COVAXIN WHERE REGNO=%s"%(regno,))
                        data=mycursor.fetchall()
                        for i in data:
                              RS=i
                        name,idno,first,second=RS[1],RS[2],RS[3],RS[4]
                        mydb.commit()
                        mycursor.execute("INSERT INTO COMPLETED VALUES('"+str(regno)+"','"+name+"','"+str(idno)+"','COVAXIN','"+str(first)+"','"+str(second)+"')")
            mydb.commit()
            mycursor.execute("SELECT* FROM COVAXIN")
        print("\nRECORDS AFTER UPDATION:\n")
        data=mycursor.fetchall()
        for i in data:
            for j in i:
                print(j,end="  ")
            print()
        mydb.commit()
    elif ch==4:
        print('''1.PRIOR APPOINTMENTS
2.VACCINES
3.PFIZER
4.MODERNA
5.COVAXIN\n''')
        ch4=int(input("ENTER THE TABLE TO DELETE RECORD FROM: "))
        print()
        if ch4==1:
            regno=int(input("ENTER REGISTRATION NUMBER: "))
            x=input('ARE YOU SURE YOU WANT TO DELETE THIS RECORD (Yes/No) ? ')
            if x=='Yes' or x=='YES':
                mycursor.execute("DELETE FROM PRIORAPPOINTMENTS WHERE REGNO=%s"%(regno,))
                mydb.commit()
                mycursor.execute("SELECT* FROM PRIORAPPOINTMENTS")
                print("\nRECORDS AFTER DELETION OPERATION:\n")
                data=mycursor.fetchall()
                for i in data:
                    for j in i:
                        print(j,end="  ")
                    print()
                mydb.commit()
            else:
                pass
        elif ch4==2:
            vac=input("ENTER VACCINE NAME: ")
            x=input('ARE YOU SURE YOU WANT TO DELETE THIS RECORD (Yes/No) ? ')
            if x=='Yes' or x=='YES':
                mycursor.execute("DELETE FROM VACCINES WHERE VACCINE=%s"%('"'+vac+'"',))
                mydb.commit()
                mycursor.execute("SELECT* FROM VACCINES")
                print("\nRECORDS AFTER DELETION OPERATION:\n")
                data=mycursor.fetchall()
                for i in data:
                    for j in i:
                        print(j,end="  ")
                    print()
                mydb.commit()
            else:
                pass
        elif ch4==3:
            regno=int(input("ENTER REGISTRATION NUMBER: "))
            x=input('ARE YOU SURE YOU WANT TO DELETE THIS RECORD (Yes/No) ? ')
            if x=='Yes' or x=='YES':
                mycursor.execute("DELETE FROM PFIZER WHERE REGNO=%s"%(regno,))
                mydb.commit()
                mycursor.execute("SELECT* FROM PFIZER")
                print("\nRECORDS AFTER DELETION OPERATION:\n")
                data=mycursor.fetchall()
                for i in data:
                    for j in i:
                        print(j,end="  ")
                    print()
                mydb.commit()
            else:
                break
        elif ch4==4:
            regno=int(input("ENTER REGISTRATION NUMBER: "))
            x=input('ARE YOU SURE YOU WANT TO DELETE THIS RECORD (Yes/No) ? ')
            if x=='Yes' or x=='YES':
                mycursor.execute("DELETE FROM MODERNA WHERE REGNO=%s"%(regno,))
                mydb.commit()
                mycursor.execute("SELECT* FROM MODERNA")
                print("\nRECORDS AFTER DELETION OPERATION:\n")
                data=mycursor.fetchall()
                for i in data:
                    for j in i:
                        print(j,end="  ")
                    print()
                mydb.commit()
            else:
                pass
        elif ch4==5:
            regno=int(input("ENTER REGISTRATION NUMBER: "))
            x=input('ARE YOU SURE YOU WANT TO DELETE THIS RECORD (Yes/No) ? ')
            if x=='Yes' or x=='YES':
                mycursor.execute("DELETE FROM COVAXIN WHERE REGNO=%s"%(regno,))
                mydb.commit()
                mycursor.execute("SELECT* FROM COVAXIN")
                print("\nRECORDS AFTER DELETION OPERATION:\n")
                data=mycursor.fetchall()
                for i in data:
                    for j in i:
                        print(j,end="  ")
                    print()
                mydb.commit()
            else:
                pass

    else:
        print("INVALID OPTION")
        
        

        
            
        
        
            
        
        
        
            
        

               
                
                
                
        
            
                    
                    
                   
            
            
                
        
        
                    
            
        
        
