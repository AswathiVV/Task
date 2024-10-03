from login import login
from admin import*
from user import *


while True:
    print('''
1.LOGIN
2.EXIT
''')
    ch=int(input("Enter Your Choice :"))
    if ch==1:
          f,user=login()
          if f==1: #admin login
            while True:
                print('''
                    1.add emp
                    2.update emp
                    3.delete
                    4.diplay
                    5.logout
                    ''')
                
                sub_choice=int(input('enter your choice: '))
                if sub_choice==1:
                    add_emp()
                elif sub_choice==2:
                    update()
                elif sub_choice==3:
                    delete()
                elif sub_choice==4:
                    display()
                elif sub_choice==5:
                    break
                else:
                    print('INVALID CHOICE')
          elif f==0:
            print('invalid username or passsword')
          elif f==2: #user login
            while True:
                if user['date_of_birth']==user['password']:
                    password=input('enter a new password')
                    user['password']=password
                else:
                    print('''
                        1.view profile
                        2.edit profile
                        3.logout
    ''')
                    sub_ch=int(input('enter your choice: '))
                    if sub_ch==1:
                        view_profile(user)
                    elif sub_ch==2:
                        user_update(user)
                    elif sub_ch==3:
                        break 
    elif ch==2:
        break  
         
                
           
              
    
        
