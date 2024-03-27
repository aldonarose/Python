print('\t               WELCOME TO JAS AIRLINES')
print('\t   please enter the number of your choice in the given spaces throughout the process ')
print()
k2=['DXB','AUH','BOM','DEL','JFK','LAX']
print('Enter 1 to book a flight')
print('Enter 2 to cancel a flight')
n=int(input('Enter your choice: '))
print()
if n==1:
    ticket={}
    a=''
    b=''
    c=''
    a2=''
    b2=''
    c2=''
    print('Our services are available in these countries \n1-United Arab Emirates \n2-India \n3-United States of America')
    x=int(input('Enter your choice: '))
    print()
    if x==1:
        print('our services are available in the following airports: \n1-Dubai International Airport(Dubai,DXB) \n2-Abudhabi International Airport(Abu Dhabi,AUH)')
        a=int(input('Enter departure airport: '))
    elif x==2:
        print('our services are available in the following airports: \n1-Chhatrapati Shivaji Maharaj International Airport(Mumbai,BOM) \n2-Indira Gandhi International Airport(Delhi,DEL)')
        b=int(input('Enter your arrival airport: '))
    elif x==3:
        print('our services are available in the following airports: \n1-John F. Kennedy International Airport(New York,JFK) \n2-Los Angeles International Airport(Los Angeles,LAX')
        c=int(input('Enter your choice: '))
    else:
        print("invalid option")    

    print()
    print('Our services are available in these countries \n1-United Arab Emirates \n2-India \n3-United States of America')
    y=int(input('Enter to where you are traveling: '))
    print()
    if y==1:
        print('our services are available in the following airports: \n1-Dubai International Airport(Dubai,DXB) \n2-Abudhabi International Airport(Abu Dhabi,AUH)')
        a2=int(input('Enter your choice: '))
    elif y==2:
        print('our services are available in the following airports: \n1-Chhatrapati Shivaji Maharaj International Airport(Mumbai,BOM) \n2-Indira Gandhi International Airport(Delhi,DEL)')
        b2=int(input('Enter your choice: '))
    elif y==3:
        print('our services are available in the following airports: \n1-John F. Kennedy International Airport(New York,JFK) \n2-Los Angeles International Airport(Los Angeles,LAX)')
        c2=int(input('Enter your choice: '))
    else:
        print("invalid option")
    print()
    g=int(input('Enter the no. of passengers, \nAdults: '))
    h=int(input('Children: '))
    i=int(input('Infants: '))
    Sum=g+h+i
    d=Sum-i
    print('Total passengers:',Sum)
    print()
    print('class:\n1.First \n2.Bussiness \n3.Economy')
    j=int(input('Enter your choice: '))
    if j==1:
        bag='50 kg per person (Excluding infants)'
        hbag=' 7kg carry-on + 7kg Briefcase or garment bag per person(Excluding infants) '
    elif j==2:
        bag='40 kg per person (Excluding infants)'
        hbag=' 7kg carry-on + 7kg Briefcase or garment bag per person(Excluding infants) '
    elif j==3:
        bag='25 kg per person (Excluding infants)'
        hbag='7kg carry-on(Excluding infants) '
    else:
        print("invalid option")

    e3=0
    e4=0
    e2=0
    if j==1:
        e2=6860
    elif j==2:
        e3=3997
    elif j==3:
        e4=0
    print()
    k=input('Enter the date (ex. 3 Jan 2020): ')
    print()
    print('\t   Searching flight.....')
    print()
    e5=0
    e6=0
    e7=0
    if (a==1) and (b2==1):
        ticket['Departure']=k2[0]
        ticket['Arrival']=k2[2]
        print('1.DXB   ----   BOM')
        print('12:45 am → 5:15 am (4h 30m)')
        e=530
        e5=(e+e2+e3+e4)*d
        print('      AED ',e5)
        print()
        print('2.DXB   ----   BOM')
        print('9:50 pm → 2:15 am (4h 25m)')
        e=603
        e6=(e+e2+e3+e4)*d
        print('      AED ',e6)
        l=int(input('Enter your choice: '))
        if l==1:
            T='JA'+str(567)    
            time='12:45 am → 5:15 am'    
            e7=e5
        else:
            T='JA'+str(157)     
            time='9:50 pm → 2:15 am'
            e7=e6    
    elif (a==1) and (b2==2):
        ticket['Departure']=k2[0]
        ticket['Arrival']=k2[3]
        print('1.DXB   ----   DEl')
        print('4:20 am → 8:55 am (4h 25m)')
        e=460
        e5=(e+e2+e3+e4)*d
        print('      AED ',e5)
        print()
        print('2.DXB   ----   DEL')
        print('11:40 pm → 4:30 am (4h 50m)')
        e=460
        e6=(e+e2+e3+e4)*d
        print('      AED ',e6)
        o=int(input('Enter your choice: '))
        if o==1:
            T='JA'+str(234)    
            time='4:20 am → 8:55 am'    
            e7=e5
        else:
            T='JA'+str(149)    
            time='11:40 pm → 4:30 am'    
            e7=e6
    elif (a==2) and (b2==1):
        ticket['Departure']=k2[1]
        ticket['Arrival']=k2[2]
        print('1.AUH   ----   BOM')
        print('8:55 pm → 1:20 am (4h 25m)')
        e=594
        e5=(e+e2+e3+e4)*d
        print('      AED ',e5)
        print()
        print('2.AUH   ----   BOM')
        print('11:45 pm → 4:35 am (4h 50m)')
        e=600
        e6=(e+e2+e3+e4)*d
        print('      AED ',e6)
        p=int(input('Enter your choice: '))
        if p==1:
            T='JA'+str(523)    
            time='8:55 pm → 1:20 am'    
            e7=e5
        else:
            T='JA'+str(241)    
            time='11:45 pm → 4:35 am'    
            e7=e6   
    elif (a==2) and (b2==2):
        ticket['Departure']=k2[1]
        ticket['Arrival']=k2[2]
        print('1.AUH   ----   DEL')
        print('12:25 am → 5:35 am (5h 10m)')
        e=340
        e5=(e+e2+e3+e4)*d
        print('      AED ',e5)
        print()
        print('2.AUH   ----   DEL')
        print('9:55 pm → 2:45 am (4h 50m)')
        e=400
        e6=(e+e2+e3+e4)*d
        print('      AED ',e6)
        q=int(input('Enter your choice: '))
        if q==1:
            T='JA'+str(507)    
            time= '12:25 am → 5:35 am'   
            e7=e5
        else:
            T='JA'+str(254)    
            time='9:55 pm → 2:45 am'    
            e7=e6
    elif (b==1) and (a2==1):
        ticket['Departure']=k2[2]
        ticket['Arrival']=k2[0]
        print('1.BOM   ----   DXB')
        print('1:20 pm → 3:00 pm (1h 40m)')
        e=444
        e5=(e+e2+e3+e4)*d
        print('      AED ',e5)
        print()
        print('2.BOM   ----   DXB')
        print('10:15 pm → 11:45 pm (1h 30m)')
        e=460
        e6=(e+e2+e3+e4)*d
        print('      AED ',e6)
        r=int(input('Enter your choice: '))
        if r==1:
            T='JA'+str(256)    
            time='1:20 pm → 3:00 pm'
            e7=e5
        else:
            T='JA'+str(258)
            time='10:15 pm → 11:45 pm'    
            e7=e6   
    elif (b==1) and (a2==2):
        ticket['Departure']=k2[2]
        ticket['Arrival']=k2[1]
        print('1.BOM   ----   AUH')
        print('8:25 pm → 10:25 pm (2h)')
        e=601
        e5=(e+e2+e3+e4)*d
        print('      AED ',e5)
        print()
        print('2.BOM   ----   AUH')
        print('2:50 am → 4:35 am (1h 45m)')
        e=620
        e6=(e+e2+e3+e4)*d
        print('      AED ',e6)
        s=int(input('Enter your choice: '))
        if s==1:
            T='JA'+str(234)    
            time='8:25 pm → 10:25 pm'
            e7=e5
        else:
            T='JA'+str(154)    
            time='2:50 am → 4:35 am'    
            e7=e6
    elif (b==2) and (a2==1):
        ticket['Departure']=k2[3]
        ticket['Arrival']=k2[0]
        print('1.DEL   ----   DXB')
        print('1:10 am → 3:25 am (2h 15m)')
        e=603
        e5=(e+e2+e3+e4)*d
        print('      AED ',e5)
        print()
        print('2.DEL   ----   DXB')
        print('8:00 pm → 10:40 pm (2h 40 m)')
        e=622
        e6=(e+e2+e3+e4)*d
        print('      AED ',e6)
        t=int(input('Enter your choice: '))
        if t==1:
            T='JA'+str(223)    
            time='1:10 am → 3:25 am'    
            e7=e5
        else:
            T='JA'+str(204)    
            time='8:00 pm → 10:40 pm'    
            e7=e6
    elif (b==2) and (a2==2):
        ticket['Departure']=k2[3]
        ticket['Arrival']=k2[0]
        print('1.DEL   ----   AUH')
        print('2:50 am → 5:40 am (3h)')
        e=650
        e5=(e+e2+e3+e4)*d
        print('      AED ',e5)
        print()
        print('2.DEL   ----   AUH')
        print('4:15 am → 6:45 am (2h 30m)')
        e=700
        e6=(e+e2+e3+e4)*d
        print('      AED ',e6)
        u=int(input('Enter your choice: '))
        if u==1:
            T='JA'+str(424)
            time='2:50 am → 5:40 am'
            e7=e5
        else:
            T='JA'+str(394)
            time='4:15 am → 6:45 am'
            e7=e6     
    elif (a==1) and (c2==1):
        ticket['Departure']=k2[0]
        ticket['Arrival']=k2[4]
        print('1 flight per day,14h 25m duration')
        print('DXB   ----   JFK')
        print('8:30 am → 1:55 pm (14h 25m)')
        e=2480
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='8:30 am → 1:55 pm (14h 25m)'
        T='JA'+str(213)
    elif (a==1) and (c2==2):
        ticket['Departure']=k2[0]
        ticket['Arrival']=k2[5]
        print('5 flights per week,16h 15m duration')
        print('DXB   ----   LAX ')
        print('8:30 am → 12:45 pm (16h 15m)')
        e=3940
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='8:30 am → 12:45 pm (16h 15m)'
        T='JA'+str(156)
    elif (a==2) and (c2==1):
        ticket['Departure']=k2[1]
        ticket['Arrival']=k2[4]
        print('5 flights per week,14h 40m duration')
        print('AUH   ----   JFK')
        print('8:10 am → 1:50 pm (14h 40m)')
        e=2720
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='8:10 am → 1:50 pm (14h 40m)'
        T='JA'+str(237)
    elif (a==2) and (c2==2):
        ticket['Departure']=k2[1]
        ticket['Arrival']=k2[5]
        print('19h 45m duration, 1+ stops')
        print('AUH   ----   LAX              2 stops')
        print('7:50 am → 8:37 pm (24h 47m)   FRA,IAD')
        e=2330
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='7:50 am → 8:37 pm (24h 47m)   FRA,IAD'
        T='JA'+str(265)
    elif (b==1) and (c2==1):
        ticket['Departure']=k2[2]
        ticket['Arrival']=k2[4]
        print('20h 10m duration, 1+ stops')
        print('BOM   ----   JFK              1 stop')
        print('2:15 am → 1:35 pm (21h 50m)  3h 35m in LHR')
        e=2869
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='2:15 am → 1:35 pm (21h 50m)  3h 35m in LHR'
        T='JA'+str(504)
    elif (b==1) and (c2==2):
        ticket['Departure']=k2[0]
        ticket['Arrival']=k2[3]
        print('22h 0m duration, 1+ stops')
        print('BOM   ----   LAX              1 stop ')
        print('4:00 am → 12:45 pm (22h 25m)  2h 5m in DOH')
        e=2893
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='4:00 am → 12:45 pm (22h 25m)  2h 5m in DOH'
        T='JA'+str(164)
    elif (b==2) and (c2==1):
        ticket['Departure']=k2[3]
        ticket['Arrival']=k2[3]
        print('3 flights per week, 15h 35m duration')
        print('DEL   ----   JFK')
        print('1:55 am → 7:00 am (15h 45m)')
        e=2342
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='1:55 am → 7:00 am (15h 45m)'
        T='JA'+str(241)
    elif (b==2) and (c2==2):
        ticket['Departure']=k2[3]

        ticket['Arrival']=k2[5]
        print('19h 2m duration, 1+ stops')
        print('DEL   ----   LAX              1 stop')
        print('4:30 am → 10:04 am (19h 4m)   2h 25m in SFO')
        e=2950
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='4:30 am → 10:04 am (19h 4m)   2h 25m in SFO'
        T='JA'+str(274)
    elif (c==1) and (a2==1):
        ticket['Departure']=k2[4]
        ticket['Arrival']=k2[0]
        print('1 flight per day, 12h 25m duration')
        print('JFK   ----   DXB ')
        print('11:00 pm → 8:25 pm (12h 27m)')
        e=2154
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='11:00 pm → 8:25 pm (12h 27m)'
        T='JA'+str(238)
    elif (c==1) and (a2==2):
        ticket['Departure']=k2[4]
        ticket['Arrival']=k2[1]
        print('5 flights per week, 12h 40m duration')
        print('JFK   ----   AUH ')
        print('9:35 pm → 7:15 pm (12h 45m)')
        e=2257
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='9:35 pm → 7:15 pm (12h 45m)'
        T='JA'+str(277)
    elif (c==2) and (a2==1):
        ticket['Departure']=k2[5]
        ticket['Arrival']=k2[0]
        print('5 flights per week, 15h 55m duration')
        print('LAX   ----   DXB ')
        print('3:35 pm → 7:30 pm (15h 55m)')
        e=2276
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='3:35 pm → 7:30 pm (15h 55m)'
        T='JA'+str(102)
    elif (c==2) and (a2==2):
        ticket['Departure']=k2[5]
        ticket['Arrival']=k2[1]
        print('19h 25m duration, 1+ stops')
        print('LAX   ----   AUH               1 stop')
        print('1:50 pm → 11:15 pm (21h 25m)   2h 5m in CDG')
        e=2661
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='1:50 pm → 11:15 pm (21h 25m)   2h 5m in CDG'
        T='JA'+str(294)
    elif (c==1) and (b2==1):
        ticket['Departure']=k2[4]
        ticket['Arrival']=k2[2]
        print('16h 30m duration, 1+ stops')
        print('JFK   ----   BOM           1 stop')
        print('9:00 pm → 2:30 am (19h)   3h 25m in DOH')
        e=2541
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='9:00 pm → 2:30 am (19h)   3h 25m in DOH'
        T='JA'+str(353)
    elif (c==1) and (b2==2):
        ticket['Departure']=k2[4]
        ticket['Arrival']=k2[3]
        print('3 flights per week, 13h 40m duration')
        print('JFK   ----   DEL ')
        print('12:30 pm → 12:40 pm (13h 40m)')
        e=2730
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='12:30 pm → 12:40 pm (13h 40m)'
        T='JA'+str(334)
    elif (c==2) and (b2==1):
        ticket['Departure']=k2[5]
        ticket['Arrival']=k2[2]
        print('20h 15m duration, 1+ stops')
        print('LAX   ----   BOM               1 stop')
        print('8:40 am → 9:40 pm (23h 30m )  3h 46m in EWR')
        e=2261
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='8:40 am → 9:40 pm (23h 30m )  3h 46m in EWR'
        T='JA'+str(456)
    elif (c==2) and (b2==2):
        ticket['Departure']=k2[5]
        ticket['Arrival']=k2[3]
        print('18h 35m duration, 1+ stops')
        print('LAX   ----   DEL               1 stop')
        print('11:00 am → 8:10 pm (19h 40m )  1h 21m in ORD ')
        e=2257
        e7=(e+e2+e3+e4)*d
        print('      AED ',e7)
        time='11:00 am → 8:10 pm (19h 40m )  1h 21m in ORD '
        T='JA'+str(454)
    else:
        print("no flights were found")
    onewayprice=e7
    total=onewayprice
    print()
    print('The Total Amount: AED',e7)
    print()
    print('Enter 1 to continue \nEnter 2 to cancel')
    cho=int(input("Enter your choice: "))
    if cho==2:
        import sys
        sys.exit()
    print()
    print('Would you like to book a return ticket?')
    tw=int(input('If Yes Enter 1, if no enter 2: '))
    if tw==1:
        Date2=input('Enter return date: ')
        print()
        if (a==1) and (b2==1):
            ticket['Departure2']=k2[2]
            ticket['Arrival2']=k2[0]
            print('1.BOM   ----   DXB')
            print('1:20 pm → 3:00 pm (1h 40m)')
            e=444
            e5=(e+e2+e3+e4)*d
            print('      AED ',e5)
            print()
            T='JA'+str(256)    
            time='1:20 pm → 3:00 pm'
            e7=e5
        elif (a==1) and (b2==2):
            ticket['Departure2']=k2[3]
            ticket['Arrival2']=k2[0]
            print('2.DEL   ----   DXB')
            print('8:00 pm → 10:40 pm (2h 40 m)')
            e=622
            e6=(e+e2+e3+e4)*d
            print('      AED ',e6)
            T='JA'+str(204)    
            time='8:00 pm → 10:40 pm'    
            e7=e6
        elif (a==2) and (b2==1):
            ticket['Departure2']=k2[2]
            ticket['Arrival2']=k2[1]
            print('1.BOM   ----   AUH')
            print('8:25 pm → 10:25 pm (2h)')
            e=601
            e5=(e+e2+e3+e4)*d
            print('      AED ',e5)
            print()
            print('2.BOM   ----   AUH')
            print('2:50 am → 4:35 am (1h 45m)')
            e=620
            e6=(e+e2+e3+e4)*d
            print('      AED ',e6)
            s=int(input('Enter your choice: '))
            if s==1:
                T='JA'+str(234)    
                time='8:25 pm → 10:25 pm'    
                e7=e5
            else:
                T='JA'+str(154)    
                time='2:50 am → 4:35 am'    
                e7=e6
        elif (a==2) and (b2==2):
            ticket['Departure2']=k2[3]
            ticket['Arrival2']=k2[0]
            print('1.DEL   ----   AUH')
            print('2:50 am → 5:40 am (3h)')
            e5=(e+e2+e3+e4)*d
            print('      AED ',e5)
            print()
            print('2.DEL   ----   AUH')
            print('4:15 am → 6:45 am (2h 30m)')
            e=700
            e6=(e+e2+e3+e4)*d
            print('      AED ',e6)
            u=int(input('Enter your choice: '))
            if u==1:
                T='JA'+str(424)
                time='2:50 am → 5:40 am'
                e7=e5
            else:
                T='JA'+str(254)    
                time='9:55 pm → 2:45 am'    
                e7=e6
        elif (b==1) and (a2==1):
            ticket['Departure2']=k2[0]
            ticket['Arrival2']=k2[2]
            print('1.DXB   ----   BOM')
            print('12:45 am → 5:15 am (4h 30m)')
            e=530
            e5=(e+e2+e3+e4)*d
            print('      AED ',e5)
            print()
            print('2.DXB   ----   BOM')
            print('9:50 pm → 2:15 am (4h 25m)')
            e=603
            e6=(e+e2+e3+e4)*d
            print('      AED ',e6)
            l=int(input('Enter your choice: '))
            if l==1:
                T='JA'+str(567)    
                time='12:45 am → 5:15 am'    
                e7=e5
            else:
                T='JA'+str(157)     
                time='9:50 pm → 2:15 am'
                e7=e6
        elif (b==1) and (a2==2):
            ticket['Departure2']=k2[1]
            ticket['Arrival2']=k2[2]
            print('1.AUH   ----   BOM')
            print('8:55 pm → 1:20 am (4h 25m)')
            e=594
            e5=(e+e2+e3+e4)*d
            print('      AED ',e5)
            print()
            print('2.AUH   ----   BOM')
            print('11:45 pm → 4:35 am (4h 50m)')
            e=600
            e6=(e+e2+e3+e4)*d
            print('      AED ',e6)
            p=int(input('Enter your choice: '))
            if p==1:
                T='JA'+str(523)
                time='8:55 pm → 1:20 am'
                e7=e5
            else:
                T='JA'+str(241)
                time='11:45 pm → 4:35 am'    
                e7=e6
        elif (b==2) and (a2==1):
            ticket['Departure2']=k2[0]
            ticket['Arrival2']=k2[3]
            print('1.DXB   ----   DEl')
            print('4:20 am → 8:55 am (4h 25m)')
            e=460
            e5=(e+e2+e3+e4)*d
            print('      AED ',e5)
            print()
            T='JA'+str(234)    
            time='4:20 am → 8:55 am'
            e7=e5
        elif (b==2) and (a2==2):
            ticket['Departure2']=k2[1]
            ticket['Arrival2']=k2[2]
            print('1.AUH   ----   DEL')
            print('12:25 am → 5:35 am (5h 10m)')
            e=340
            e5=(e+e2+e3+e4)*d
            print('      AED ',e5)
            print()
            print('2.AUH   ----   DEL')
            print('9:55 pm → 2:45 am (4h 50m)')
            e=400
            e6=(e+e2+e3+e4)*d
            print('      AED ',e6)
            q=int(input('Enter your choice: '))
            if q==1:
                T='JA'+str(507)    
                time= '12:25 am → 5:35 am'   
                e7=e5
            else:
                T='JA'+str(254)    
                time='9:55 pm → 2:45 am'    
                e7=e6
        elif (a==1) and (c2==1):
            ticket['Departure2']=k2[4]
            ticket['Arrival2']=k2[0]
            print('1 flight per day, 12h 25m duration')
            print('JFK   ----   DXB ')
            print('11:00 pm → 8:25 pm (12h 27m)')
            e=2154
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='11:00 pm → 8:25 pm (12h 27m)'
            T='JA'+str(238)
        elif (a==1) and (c2==2):
            ticket['Departure2']=k2[5]
            ticket['Arrival2']=k2[0]
            print('5 flights per week, 15h 55m duration')
            print('LAX   ----   DXB ')
            print('3:35 pm → 7:30 pm (15h 55m)')
            e=2276
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='3:35 pm → 7:30 pm (15h 55m)'
            T='JA'+str(102)
        elif (a==2) and (c2==1):
            ticket['Departure2']=k2[4]
            ticket['Arrival2']=k2[1]
            print('5 flights per week, 12h 40m duration')
            print('JFK   ----   AUH ')
            print('9:35 pm → 7:15 pm (12h 45m)')
            e=2257
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='9:35 pm → 7:15 pm (12h 45m)'
            T='JA'+str(277)
        elif (a==2) and (c2==2):
            ticket['Departure2']=k2[5]
            ticket['Arrival2']=k2[1]
            print('19h 25m duration, 1+ stops')
            print('LAX   ----   AUH               1 stop')
            print('1:50 pm → 11:15 pm (21h 25m)   2h 5m in CDG')
            e=2661
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='1:50 pm → 11:15 pm (21h 25m)   2h 5m in CDG'
            T='JA'+str(294)
        elif (b==1) and (c2==1):
            ticket['Departure2']=k2[4]
            ticket['Arrival2']=k2[2]
            print('16h 30m duration, 1+ stops')
            print('JFK   ----   BOM           1 stop')
            print('9:00 pm → 2:30 am (19h)   3h 25m in DOH')
            e=2541
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='9:00 pm → 2:30 am (19h)   3h 25m in DOH'
            T='JA'+str(353)
        elif (b==1) and (c2==2):
            ticket['Departure2']=k2[5]
            ticket['Arrival2']=k2[2]
            print('20h 15m duration, 1+ stops')
            print('LAX   ----   BOM               1 stop')
            print('8:40 am → 9:40 pm (23h 30m )  3h 46m in EWR')
            e=2261
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='8:40 am → 9:40 pm (23h 30m )  3h 46m in EWR'
            T='JA'+str(456)
        elif (b==2) and (c2==1):
            ticket['Departure2']=k2[4]
            ticket['Arrival2']=k2[3]
            print('3 flights per week, 13h 40m duration')
            print('JFK   ----   DEL ')
            print('12:30 pm → 12:40 pm (13h 40m)')
            e=2730
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='12:30 pm → 12:40 pm (13h 40m)'
            T='JA'+str(334)
        elif (b==2) and (c2==2):
            ticket['Departure2']=k2[5]
            ticket['Arrival2']=k2[3]
            print('18h 35m duration, 1+ stops')
            print('LAX   ----   DEL               1 stop')
            print('11:00 am → 8:10 pm (19h 40m )  1h 21m in ORD ')
            e=2257
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='11:00 am → 8:10 pm (19h 40m )  1h 21m in ORD '
            T='JA'+str(454)
        elif (c==1) and (a2==1):
            ticket['Departure2']=k2[0]
            ticket['Arrival2']=k2[4]
            print('1 flight per day,14h 25m duration')
            print('DXB   ----   JFK')
            print('8:30 am → 1:55 pm (14h 25m)')
            e=2480
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='8:30 am → 1:55 pm (14h 25m)'
            T='JA'+str(213)
        elif (c==1) and (a2==2):
            ticket['Departure2']=k2[1]
            ticket['Arrival2']=k2[4]
            print('5 flights per week,14h 40m duration')
            print('AUH   ----   JFK')
            print('8:10 am → 1:50 pm (14h 40m)')
            e=2720
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='8:10 am → 1:50 pm (14h 40m)'
            T='JA'+str(237)
        elif (c==1) and (b2==1):
            ticket['Departure2']=k2[2]
            ticket['Arrival2']=k2[4]
            print('20h 10m duration, 1+ stops')
            print('BOM   ----   JFK              1 stop')
            print('2:15 am → 1:35 pm (21h 50m)  3h 35m in LHR')
            e=2869
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='2:15 am → 1:35 pm (21h 50m)  3h 35m in LHR'
            T='JA'+str(504)
        elif (c==1) and (b2==2):
            ticket['Departure2']=k2[3]
            ticket['Arrival2']=k2[3]
            print('3 flights per week, 15h 35m duration')
            print('DEL   ----   JFK')
            print('1:55 am → 7:00 am (15h 45m)')
            e=2342
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='1:55 am → 7:00 am (15h 45m)'
            T='JA'+str(241)
        elif (c==2) and (b2==1):
            ticket['Departure2']=k2[0]
            ticket['Arrival2']=k2[3]
            print('22h 0m duration, 1+ stops')
            print('BOM   ----   LAX              1 stop ')
            print('4:00 am → 12:45 pm (22h 25m)  2h 5m in DOH')
            e=2893
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='4:00 am → 12:45 pm (22h 25m)  2h 5m in DOH'
            T='JA'+str(164)
        elif (c==2) and (b2==2):
            ticket['Departure2']=k2[3]
            ticket['Arrival2']=k2[5]
            print('19h 2m duration, 1+ stops')
            print('DEL   ----   LAX              1 stop')
            print('4:30 am → 10:04 am (19h 4m)   2h 25m in SFO')
            e=2950
            e7=(e+e2+e3+e4)*d
            print('      AED ',e7)
            time='4:30 am → 10:04 am (19h 4m)   2h 25m in SFO'
            T='JA'+str(274)
        else:
            print("no flights were found")
        Returnprice=e7
        total=total+Returnprice
        print('Return price: ',Returnprice)
        print('Enter 1 to continue \nEnter 2 to cancel return ticket')
        cho2=int(input("Enter your choice: "))
        if cho2==2:
            total=onewayprice 
            print("--------------------------------------------------- One way only--------------------------------------------- \nThe Total Amount: AED ",onewayprice)
        else:
            print("--------------------------------------------------- Two way--------------------------------------------- \nThe Total Amount: AED ",total)
        print()
        print('                                  BAGGAGE ALLOWANCE                                ')
        print('Checked baggage: ',bag,'\nCabin baggage: ',hbag)
        print()
        ebag=int(input("Enter 1 to add extra baggage (for departure only i.e, extra baggage not included in return trip):" ))
        if ebag==1:
            print('''Enter 1 to add 3kg (+180 AED)
Enter 2 to add 5 kg (+250 AED)''')
            ald=int(input("Enter your choice: "))
            if ald==1:
                total=total+180
                ticket['baggageextras']='3kg'
            elif ald==2:
                total=total+250
                ticket['baggageextras']='5kg'
            else:
                print("invalid option")
        else:
            ticket['baggageextras']='-'
        print("-------------------------------------------FOOD OPTIONS----------------------------------------------")
        print()
        FOOD=int(input("If you wish to pre order your inflight food enter 1: "))
        if FOOD==1:
            gh= g+h
            kiddo= h+i
            print('     MEAL CHOICES   ')
            if j==1 or j==2:
                for pop in range (g):
                    print('''Enter 1 for vegetarian meal choices
Enter 2 for non-vegetarian meal choices''')
                    food=int(input("Enter your choice: "))
                    if food==1:
                        vegd={1:150,2:150,3:90,4:180,5:120,6:0}
                        print('''        VEGETARIAN MENU
1-Bland meal                                      AED 150
2-Diabetic meal                                   AED 150
3-Low-calorie meal                                AED 90
4-Vegetarian oriental meal (chinese style)        AED 180
5-Vegetarian jain meal (indian style)             AED 120
6-Vegetarian meal                                 AED 00 ''')
                        veg=int(input("Enter your choice: "))
                        total=total+vegd[veg]
                        ticket['vegfoodchoice']= veg
                        print()
                    elif food==2 :
                        nvd={1:160,2:150,3:150,4:155,5:160,6:160,7:0,}
                        print('''            NON-VEG MENU
1-Bland meal                                      AED 160
2-Diabetic meal                                   AED 150
3-Gluten free meal                                AED 150
4-Low-calorie meal                                AED 155
5-Low fat / low cholesterol meal                  AED 160
6-Lactose-free meal                               AED 160
7-Non-veg meal                                   AED 00 ''')
                        nonveg=int(input("Enter your choice: "))
                        total=total+nvd[nonveg]
                        ticket['non-vegfoodchoice']= nonveg
                    print()
                if i or h !=0:
                    
                    bby=input("would you like to add kid's/baby food?: ")
                    
                print()
                if bby=='yes' or 'Yes' or 'YES':
                         kdfd={1:80,2:100,3:90,4:120}
                         print('''     KIDS MENU
1-Baby's meal                                       AED 80
2-Kid's meal (Non-vegetarian)                     AED 100
3-Kid's meal (Vegetarian)                         AED 90
4-Lactose-free meal                               AED 120 ''')
                         for x in range (kiddo):
                             kdf=int(input("enter your choice: "))
                             total=total+kdfd[kdf]
                             ticket['kid-foodchoice']= kdf
                             print()
                            
            elif j==3:
                for pop in range (gh):
                    print('''Enter 1 for vegetarian meal                 AED 15 
Enter 2 for non-vegetarian meal             AED 15''')
                    food=int(input("Enter your choice: "))
                    if food==1 or food==2:
                        total=total+15
                        print()
                        if food==2:
                            print('''Enter 1 for fish
Enter 2 for meat''')
                            fm=int(input("Enter your choice: "))
            print()
            print("If you wish to order extras, you can do so on-board")
            print('--------------------------------------------------------------------------------')
        else:
            ticket['FOOD']='NO'
            print("If you wish to order extras, you can do so on-board")
        Care=input("Enter 1 if you require any special care or assistance: ")
        if int(Care)==1:
            ticket['Special Care']='Yes'
            print("please contact your local JAS Airlines office after booking to advise us of your requirements.")
        else:
            ticket['Special Care']='No'
        print()
        print()
        print('\n','The Total Amount: AED',total)        
        print("-------------------------------------Total price includes tax----------------------------------------")
        print()
        print()
        print('\t   PAYMENT DETAILS')
        print()
        print('1. Credit Card')
        print('2. Debit Card')
        i1=int(input('Enter your choice: '))
        j1=int(input('Enter the card number: '))
        k1=input('Enter the cardholder\'s name: ')
        l1=input('Expiry date: ')
        m1=int(input('Enter the Security code(CVV): '))
        import random
        pnr= 'J'+'A'+str(k[0])+str(random.randrange(0,10))+str(random.randrange(0,10))+str(random.randrange(0,10))+str(random.randrange(0,10))
        tn='195'+pnr[2:6]+T[2:5]+str(random.randrange(0,10))+str(random.randrange(0,10))
        if ticket['Departure'] or ticket['Departure2'] in ['DXB','AUH','BOM']:
            terminal='Terminal 1'
        else:
            terminal='Terminal 2'
        print()
        print('\t    PASSENGER DETAILS')
        print()
        h1=1        
        while h1<=Sum:
            v=input('Enter your First Name: ')
            w=input('Enter your Surname: ')
            z=input('Enter your Gender: ')
            a1=input('Email: ')
            b1=input('Address: ')
            c1=input('City: ')
            d1=input('Country: ')
            xl=input('Nationality: ')
            e1=input('Postcode: ')
            f1=input('Country code: ')
            g1=input('Phone no.: ')
            p2=int(input("Passport no: "))
            h1=h1+1
            ticket[w+'/'+v]=[T,z,a1,b1,c1,d1,xl,e1,f1,g1,p2]
            print()
            print("Enter 1 to confirm your booking \n Enter 2 to cancel your booking")
            choice=int(input("Enter your choice: "))
            if choice==1:
                ticket['information']=[pnr,tn,i1,j1,k1,l1,m1,terminal]
                print()
                print('                                         E- TICKET                                    ')
                print()
                print('Booking Reference:',pnr,'\n','Ticket number:', tn,'\n', 'flight: ', T, '\n','Departure \t Arrival \n',ticket['Departure'], '\t', ticket['Arrival'], '\n', time, '\n','Date:',k,'\n', 'Name:', w,'/',v, '\n', 'Nationality:', xl, '\n', terminal)
                if tw==1 and cho2==1:
                    print()
                    print('flight: ', T, '\n','Departure \t Arrival \n',ticket['Departure2'], '\t', ticket['Arrival2'], '\n', time, '\n','Date:',Date2,'\n', 'Name:', w,'/',v, '\n', 'Nationality:', xl, '\n', terminal)
                else:
                    del ticket
                myticket={}
                myticket=ticket.copy()
                print()
                print('\t    YOUR FLIGHT IS BOOKED')
                print('\t       THAKYOU')
elif n==2:
    Cancelledtickets={}
    PNR=input("Booking reference: ")
    TN=input("Enter ticket number: ")
    fname=input("Enter first name: ")
    lname=input("Enter last name: ")
    Cancelledtickets[PNR]=str(PNR)+'ticket'
    print("Your ticket ",str(PNR)+'ticket', " has been added to the cancellation list, please contact your local JAS airlines office for the return payment details")
