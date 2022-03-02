import random
import csv
import os

try:
    f=open('booking.csv','x',newline='')
    f.close()
    f=open('booking.csv','w',newline='')
    w.writerow(['room no','room type','room size ',' extra beds ',' couch  ','    tv   ','number of days'])
    f.close()
    
except:
    s=open("booking.csv","r")
    rno=100
    c=csv.reader(s)
    j=0
    for i in c:
        j=j+1
    
    rno=99+j
    print('file already exists')
    s.close()

def pricelist():
    print('\t________________________________________________\n\n')
    print('*COSTS ARE CALCULATED FOR 12 HOURS*')
    print('*EXCLUSIVE OF FOOD COSTS*')
    print('SMALL SIZED ROOM-RS 399')
    print('MEDIUM SIZED ROOM-RS 599')
    print('LARGE SIZED ROOM-RS699')
    print('EXTRA BED COSTS RS 99 EACH')
    print('ROOM WITH AC COSTS RS 99 EXTRA')
    print('ADDITIONAL TV ONLY AVAILABLE FOR LARGE ROOMS AND COST 39 EXTRA')
    

def booking():
    f=open('booking.csv','a',newline='')
    w=csv.writer(f)
    print('\t________________________________________________\n\n')
    print('\t\t BOOKING \n\n')
    global rno
    sz=str(input('what size of room would you like small/medium/large?'))
    da=str(input("for how many days would you like a room?"))
    ac=str(input('what room would you like? ac/nonac?'))    
    nb=str(input('how many extra beds would you need? 0/1?'))
    tv=str(input('would you like to have a tv yes/no?'))
    co=str(input('would you like a couch yes/no?'))
    l=[str(rno),ac,sz,nb,co,tv,da]
    l1=[]
    for i in l:
        a=len(i)+10
        b=i.center(a)
        l1.append(b)
                              
    w.writerow(l1)
    rno=int(rno)+1
    f.close()
                      
    f1=open('booking.csv','r')
    r=csv.reader(f1)
    for i in r:
        print(i)
    print('booking confirmed')

def foodmenu():
    print('SOUPS')
    print('\n')
    print('TOMATO                                                   Rs.75')
    print('CREAMY SWEET CORN                                        Rs.80')
    print('''PEPPY MUSHROOM (chef's special)                          Rs.90 ''')
    print('HOT N SOUR (VEG/CHICKEN)                                 Rs.80/Rs.100')
    print('CHEESY MANCHOW  (VEG/CHICKEN)                            Rs.90/Rs.120')
    print('MAKE YOU OWN SOUP                                        starts from Rs.90')
    print('\n')
    print('\n')
    print('STARTERS')
    print('\n')
    print('VEG MANCHURIAN                                           Rs.99')
    print('GOBI 65                                                  Rs.109')
    print('PANEER 65                                                Rs.149')
    print('CRISPY CORN                                              Rs.119')
    print('GOBI MANCHURIAN                                          Rs.119')
    print('PANEER MANCHURIAN                                        Rs.159')
    print('CHILLY PANEER                                            Rs.159')
    print('PEPPY PANEER                                             Rs.159')
    print('CHICKEN 65                                               Rs.179')
    print('CHILLY CHICKEN                                           Rs.169')
    print('GARLIC CHICKEN                                           Rs.169')
    print('CHILLY PRAWN                                             Rs.189')
    print('''MUTTON CHUKKA  (CHEF'S SPECIAL)                          Rs.199''')
    print('''DEVIL'S FAVORITE  (CHEF'S SPECIAL (Must Try))            Rs.249''')
    print('\n')
    print('\n')
    print('MAIN COURSE')
    print('\n')
    print('BIRIYANI  (VEG/CHCIKEN/PRAWN/MUTTON)                     Rs.120/Rs.180/Rs.200/Rs.250')
    print('FRIED RICE  (VEG/EGG/CHICKEN/PRAWN)                      Rs.90/Rs.99/Rs.109/Rs.129')
    print('AMERICAN CHOPSEUY (VEG/CHICKEN)                          Rs.150/Rs.200')
    print('SAMBAR RICE                                              Rs.70')
    print('CURD RICE                                                Rs.70')
    print('VARIETY RICE                                             Rs.80')
    print('''AUTHENTIC KERALA PUTTU    (CHEF'S SPECIAL)               Rs.199''')
    print('\n')
    print('\n')
    print('HI-TEA & CHAATS  ')
    print('\n')
    print('TEA                                                      Rs.15')
    print('COFFEE                                                   Rs.15')
    print('MILK                                                     Rs.15')
    print('BOOST                                                    Rs.15')
    print('GREEN TEA                                                Rs.20')
    print('BLACK TEA                                                Rs.20')
    print('GINGER TEA                                               Rs.20')
    print('MASALA TEA                                               Rs.20')
    print('BONDA                                                    Rs.30')
    print('VADA                                                     Rs.25')
    print('BAJJI (CHILLI/POTATO/ONION/BANANA)                       Rs.30')
    print('VEG ROLL                                                 Rs.45')
    print('CHICKEN ROLL                                             Rs.50')
    print('SPRING ROLL (VEG/NON-VEG)                                Rs.35/Rs.45')
    print('PAANI POORI                                              Rs.30')
    print('BHEL PURI                                                Rs.35')
    print('PAV BHAJI                                                Rs.50')
    print('VADA PAV                                                 Rs.30')
    print('DAHI POORI                                               Rs.50')
    print('MASALA POORI                                             Rs.40')
    print('PAPDI CHAAT                                              Rs.45')
    print('CHANNA MASALA                                            Rs.50')
    print('SAMOSA                                                   Rs.10')
    print('CUTLET                                                   Rs.15')
    print('KACHORI                                                  Rs.25')
    print('CHANNA SAMOSA                                            Rs.55')
    print('CHANNA CUTLET                                            Rs.60')
    print('CHANNA KACHORI                                           Rs.60')
    print('DAHI PAPDI CHAAT                                         Rs.55')
    print('SPECIAL PAV BHAJI                                        Rs.80')
    print('\n')
    print('\n')
    print('BREADS')
    print('\n')
    print('NAAN                                                     Rs.40')
    print('BUTTER NAAN                                              Rs.50')
    print('GARLIC NAAN                                              Rs.60')
    print('KULCHA                                                   Rs.40')
    print('BUTTER KULCHA                                            Rs.50')
    print('MASALA KULCHA                                            Rs.70')
    print('CHEESE MASALA KULCHA                                     Rs.90')
    print('KUBOOS                                                   Rs.20')
    print('ROTI                                                     Rs.30')
    print('TANDOORI ROTI                                            Rs.35')
    print('ALOO PARATHA                                             Rs.60')
    print('PARATHA                                                  Rs.30')
    print('STUFFED NAAN                                             Rs.80')
    print('\n')
    print('\n')
    print('ARABIAN DELIGHTS')
    print('\n')
    print('SHAWARMA (ROLL/PLATE)                                    Rs.70/Rs.130')
    print('MEXICAN SHAWARMA  (ROLL/PLATE)                           Rs.80/Rs.140')
    print('CHEESY JALAPENO SHAWARMA  (ROLL/PLATE)                   Rs.90/Rs.150')
    print('BBQ SHAWARMA  (ROLL/PLATE)                               Rs.80/Rs.140')
    print('ALFAHAM DEJAJ CHICKEN (HALF/FULL)                        Rs.180/Rs.320')
    print('\n')
    print('\n')
    print('GRILL & TANDOOR')
    print('\n')
    print('TANDOORI PANEER                                          Rs.200')
    print('TANDOORI CHICKEN (HALF/FULL)                             Rs.160/Rs.300')
    print('GRILL CHICKEN (HALF/FULL)                                Rs.160/Rs.300')
    print('\n')
    print('\n')
    print('BARBEQUE')
    print('\n')
    print('BBQ CHICKEN (HALF/FULL)                                  Rs.200/Rs.360')
    print('SPICY BBQ CHICKEN (HALF/FULL)                            Rs.210/Rs.370')
    print('PEPPER BBQ CHICKEN                                       Rs.210/Rs.380')
    print('CHEESY BBQ CHICKEN                                       Rs.220/Rs.400')
    print('BBQ PANEER                                               Rs.220')
    print('BBQ FISH                                                 Rs.320')
    print('BBQ MUSHROOM                                             Rs.160')
    print('EXTRA KUBOOS                                             Rs.10')
    print('\n')
    print('\n')
    print('JUICES & DESSERTS')
    print('\n')
    print('APPLE                                                    Rs.70')
    print('WATERMELON                                               Rs.50')
    print('PINEAPPLE                                                Rs.60')
    print('MUSKMELON                                                Rs.60')
    print('LEMON                                                    Rs.40')
    print('SWEET LIME                                               Rs.70')
    print('DRAGON FRUIT                                             Rs.100')
    print('FIG                                                      Rs.70')
    print('BUTTER FRUIT                                             Rs.90')
    print('STRAWBERRY                                               Rs.100')
    print('ORANGE                                                   Rs.80')
    print('POMOGRANATE                                              Rs.80')
    print('\n')
    print('VANNILA                                                  Rs.80')
    print('STRAWBERRY                                               Rs.75')
    print('BUTTERSCOTCH                                             Rs.90')
    print('CHOCOLATE                                                Rs.100')
    print('DARK CHOCOLATE                                           Rs.110')
    print('BLACK CURRENT                                            Rs.110')
    print('MANGO                                                    Rs.110')
    print('PISTA                                                    Rs.90')
    print('CASSATA                                                  Rs.120')
    print('ORANGE                                                   Rs.90')
    print('''COOKIE AND CREME     (CHEF'S SPECIAL)                    Rs.150''')
    print('\n')
    print('\n')
    print('\n')
    print('''    Price You See Is The Price You Pay.
    No Hidden Charges.
    Kindly call and place your order from your room
    special instructions can be conveyed while ordering.''')
    print('\n')
    print('\n')
    print('\n')
    print('\n')
    print('HAPPY BINGEING')
    print('\n')
    print('\n')

def payment():
    sum=0
    r=str(input('enter your room number'))
    f=open("booking.csv","r",newline='')
    s=csv.reader(f)
    next (s)
    for i in s:
        if(int(i[0])==int(r)):         
            
            if(i[1].strip()=='ac'):                
                sum=sum+99
            if(i[2].strip()=='small'):                
                sum+=399
            if(i[2].strip()=='medium'):               
                sum+=599
            if(i[2].strip()=='large'):
                if(i[5].strip()=='no'):                    
                    sum+=699
                elif(i[5].strip()=='yes'):
                     sum=sum+699+39             
            if(i[3].strip()=='1'):                
                sum+=99            
            total=sum*(int(i[6])*2)    
    print('room no',r,'your bill amount is',total)
    f.close()


def checkout():
    org=open("booking.csv","r",newline='')
    temp=open("checkout.csv","w",newline='')
    dat=csv.reader(org)
    c=csv.writer(temp)
    rnooo=str(input('enter the room number to be checked out'))
    next (dat)
    t=0
    q=0
    for i in dat:
        t=t+1
        if(int(i[0])!=int(rnooo)):
            q+=1
            if(t!=q):
                i[0]=99+t
                c.writerow(i)
            else:
                c.writerow(i)
            
    org.close()
    temp.close()
    os.remove("booking.csv")
    os.rename("checkout.csv","booking.csv")  

def menu():
    print('\t________________________________________________\n\n')
    print('\t\t WELCOME TO HOTEL XYZ\n\n')
    print('\t________________________________________________\n\n')
    print('1.PRICE LIST')
    print('2.BOOKING')
    print('3.FOOD MENU')
    print('4.PAYMENT')
    print('5.CHECKOUT')
    
    ch=int(input("enter your choice")) 

    if(ch==1):
        print(" ")
        print('\t________________________________________________\n\n')
        pricelist()

    if(ch==2):
        print(" ")
        print('\t________________________________________________\n\n')
        booking()

    if(ch==3):
        print('')
        print('\t________________________________________________\n\n')
        foodmenu()

    if(ch==4):
        print('')
        print('\t________________________________________________\n\n')
        payment()

    if(ch==5):
        print('')
        print('\t________________________________________________\n\n')
        checkout()

   
        
while True:
    menu()
    print('\n\n')
    CH=str(input('would you like continue y/n?'))
    if(CH!='y'):
        break
