import random

def questPassw(quess):# Enter the level of password
    if quess =='1':# length of password 6
        password=(''.join([random.choice(list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (6)]))
    elif quess=='2':# length of password 9
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (9)]))
    elif quess=='3':# length of password 12
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (12)]))
    else:
       print('ERROR')
       quess=input('How Secure must have 1-Easy/2-Stron/3-Very Strong : ')
       password=questPassw(quess)
    return password

def questPasswEnd(quess,customtext):#add custom text in the end of the password
    ct=customtext
    if quess =='1':
        password=(''.join([random.choice(list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (6-len(ct))])+ct)
    elif quess=='2':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (9-len(ct))])+ct)
    elif quess=='3':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (12-len(ct))])+ct)
    else:
       print('ERROR')
       quess=input('How Secure must have 1-Easy/2-Stron/3-Very Strong : ')
       password=questPassw(quess,ct)
    return password

# add custom text to the password
def questPasswStart(quess,customtext):# add custom text in the start of the password
    ct=customtext
    if quess =='1':
        password=(ct+''.join([random.choice(list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (6-len(ct))]))
    elif quess=='2':
        password=(ct+''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (9-len(ct))]))
    elif quess=='3':
        password=(ct+''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (12-len(ct))]))
    else:
       print('ERROR')
       quess=input('How Secure must have 1-Easy/2-Stron/3-Very Strong : ')
       password=questPassw(quess,ct)
    return password

def questPasswMix(quess,customtext):#add custom text in the middle of the password
    ct=customtext
    if quess =='1':
        password=(''.join([random.choice(list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (6)]))
        password=password[:3]+ct+password[3:]
    elif quess=='2':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (9)]))
        password=password[:5]+ct+password[5:]
    elif quess=='3':
        password=(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*'))for x in range (12)]))
        password=password[:8]+ct+password[8:]
    else:
       print('ERROR')
       quess=input('How Secure must have 1-Easy/2-Stron/3-Very Strong : ')
       password=questPassw(quess,ct)
    return password

def informationAboutPassword(a):#it gives information about password 
    countNumber=0
    countLitle=0
    countBig=0
    countSpecial=0
    listBLetter=[]
    listSmallLette=[]
    listNumber=[]
    listSpecial=[]
    print("Size your password = {}".format(len(a)))
    print("Your password start with = {}".format(a[0]))
    print("The end your password  = {}".format(a[-1]))
    print("Your password = {} ".format(a))
    
    
    for j in range(0,len(a)):
        for i in ['0','1','2','3','4','5','6','7','8','9']:
            if(a[j]==i):
               listNumber.append(i)
               countNumber=countNumber+1
                
    print ("Number of digits in the password ={} ".format(countNumber))
    print("Your password has a digits={}".format(listNumber))
    

    for j in range(0,len(a)):
        for i in ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
            if(a[j]==i):
                listSmallLette.append(i)
                countLitle=countLitle+1
                
    print ("Number of little letters  in the password = {}".format(countLitle))
    print("Your password has a little letter = {}".format(listSmallLette))
    
    
    for j in range(0,len(a)):
        for i in ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']:
            if(a[j]==i):
                listBLetter.append(i)
                countBig=countBig+1
                
    print ("Number of Big letters  in the password = {}".format(countBig))
    print("Your password has a big letter ={}".format(listBLetter))
    
    
    for j in range(0,len(a)):
        for i in ['!','@','#','$','%','^','&','*']:
            if(a[j]==i):
                listSpecial.append(i)
                countSpecial=countSpecial+1
    
    print("Number of special characters in the password = {}".format(countSpecial))
    print("Your password has a special character = {}".format(listSpecial))
    
    
    
    
    
    
    
#def funHello():
print('Hello, friend :)')
name=input('What is your name ? ')
print('{} ,nice to meet you '.format(name))
    
#ask user to choose the strength of the password
quess=input('How Secure must have 1-Easy/2-Stron/3-Very Strong : ')
#ask user to choose an option to add custom text
choice=(int(input("if you want combine with custom text 1-Yes 2-No : ")))
if choice==1:
    customtext=str(input("Enter Custom Text : "))
    check=(int(input("if password \"End with your custom text Enter 1\" \" Start with your custom text Enter 2\" \"Mix with custom text Enter 3\" :")))
    if check==1:
        yourPassword=questPasswEnd(quess,customtext)
    if check==2:
        yourPassword=questPasswStart(quess,customtext)
    if check==3:
        yourPassword=questPasswMix(quess,customtext)
elif choice==2:
    yourPassword=questPassw(quess)
else:
    print("error choice")
question= input('Do you want show on the screen your password (yes/no)?')
if (question == 'yes'):
    informationAboutPassword(yourPassword)
else:
     print('See you late :)')