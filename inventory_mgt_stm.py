import datetime
print(datetime.datetime.now().strftime("%x"))
inv=[]
sup=[]
rep=[]
while True:
    print('''
1. ADD ITEM
2. VIEW INVENTORY
3. UPDATE ITEM
4. REMOVE ITEM
5. MANAGE SUPPLIERS
6. GENERATE REPORTS
7. SEARCH ITEM
8. EXIT
''')
    choice=int(input("ENTER YOUR CHOICE :"))
    if choice==1:
        name =input("Item Name: ")
        id = int(input("ID: "))
        category = input("Category: ")
        quantity = int(input("Quantity: "))
        supplier = input("Supplier: ")
        date = datetime.datetime.now().strftime("%x")
        inv.append({'name':name,'id':id,'category':category,'quantity':quantity,'supplier':supplier,'date':date})
    elif choice==2:
        print('_'*75)
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('name','id','category','quantity','supplier','date'))    
        print('_'*75)
        for i in inv:
            print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['name'],i['id'],i['category'],i['quantity'],i['supplier'],i['date']))
    elif choice==3:
        id = int(input("ID: "))
        f=0
        for i in inv:
            if i['id']==id:
                f=1
                while True:
                     print('''
1. UPDATE NAME
2. UPDATE CATEGORY
3. UPDATE QUANTITY
4. UPDATE SUPPLIER
5. EXIT
''')
                     
                     sub_choice = int(input("Enter your choice: "))
                     if sub_choice==1:
                        new_name=input("Enter New Name :")
                        i['name']=new_name
                     elif sub_choice==2:
                        new_category=input("Enter New Category :")
                        i['category']=new_category
                     elif sub_choice==3:
                        new_quantity=int(input("Enter New Quantity :"))
                        i['quantity']
                     elif sub_choice==4:
                        new_quantity=input("Enter New Supplier :")
                        i['supplier']
                     elif sub_choice==5:
                        break         
        if f==0:
            print('ID NOT FOUND') 
    elif choice==4:
        id=int(input("Enter ID :"))   
        f=0
        for i in inv:
            if i['id']==id:
                inv.remove(i) 
                f=1
                print("ITEM REMOVED SUCCESSFULLY")
        if f==0:
            print("ID NOT FOUND")     
    elif choice==5:
        id=int(input("Enter Your Admin ID :"))
        while True:
         print('''
1. ADD SUPPLIER
2. VIEW SUPPLIERS
3. UPDATE SUPPLIERS
4. REMOVE SUPPLIERS           
5. EXIT
        ''')
         choice = int(input("Enter your choice: "))
         if choice == 1:
            id=int(input("ID :"))
            name = input("Supplier Name: ")
            contact = input("Contact Information: ")
            address = input("Address: ")
            date = datetime.datetime.now().strftime("%x")
            sup.append({'id':id,'name':name,'contact':contact,'address':address,'date':date})
         elif choice == 2:
            print('_' * 100)
            print('{:<10}{:<20}{:<30}{:<30}{:<10}'.format('id','name', 'contact', 'address', 'date'))
            print('_' * 100)
            for i in sup:
                print('{:<10}{:<20}{:<30}{:<30}{:<10}'.format(i['id'],i['name'], i['contact'], i['address'], i['date']))
         elif choice==3:
               id = int(input("ENTER YOUR ADMIN ID: "))
               f=0
               for i in sup:
                  
                    while True:
                     print('''
1. UPDATE NAME
2. UPDATE CONTACT
3. UPDATE ADDRESS
4. UPDATE DATE
5. EXIT
''')
                     
                     sub_choice = int(input("Enter your choice: "))
                     if sub_choice==1:
                        new_name=input("Enter New Name :")
                        i['name']=new_name
                     elif sub_choice==2:
                        new_contact=input("Enter New Contact :")
                        i['contact']=new_contact
                     elif sub_choice==3:
                        new_address=input("Enter New Address :")
                        i['address']
                     elif sub_choice==4:
                        date = datetime.datetime.now().strftime("%x")
                     elif sub_choice==5:
                        break         
                     else:
                        print('ID NOT FOUND') 
         elif choice==4:
             id=int(input("Enter ID :"))   
             f=0
             for i in sup:
              if i['id']==id:
                sup.remove(i) 
                f=1
                print("ITEM REMOVED SUCCESSFULLY")
             if f==0:
                print("ID NOT FOUND")  

         elif choice == 5:
            break
    elif choice==6:
        for i in rep:
            while True:
                     print('''
1. EXECUTIVE SUMMARY
2. INVENTORY OVERVIEW
3. STOCK LEVELS
4. PURCHASE & SALES DATA
5. INVENTORY ACCURACY   
6. SUPPLIER & VENDOR PERFORMANCE
7. COST ANALYSIS
8. FORECASTING & PLANNING
9. RECOMMENDATIONS
10.APPENDICES                                                                                                                                                              

''')
                     
        sum =input("EXECUTIVE SUMMARY :")
        over = input("INVENTORY OVERVIEW : ")
        lev = input("STOCK LEVELS : ")
        pur = input("PURCHASE & SALES DATA : ")
        accu = input("INVENTORY ACCURACY : ")
        per=input("SUPPLIER & VENDOR PERFORMANCE :")
        cost=input("COST ANALYSIS :")
        pln=input("FORECASTING & PLANNING :")
        rec=input("RECOMMENDATIONS :") 
        app=input("APPENDICES :") 
        date = datetime.datetime.now().strftime("%x")
        rep.append({'sum':sum,'over':over,'lev':lev,'pur':pur,'accu':accu,'per':per,'cost':cost,'pln':pln,'rec':rec,'app':app,'date':date})

        print('_'*125)
        print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('sum','over','lev','pur','accu','per','cost','pln','rec','app','date'))    
        print('_'*125)
        for i in rep:
            print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(i['sum'],i['over'],i['lev'],i['pur'],i['accu'],i['per'],i['cost'],i['pln'],i['rec'],i['app'],i['date']))

    elif choice==7 :
        id = int(input("Enter Item ID to search: "))
        f= 0
        for i in inv:
          if i['id'] == id:
            f = 1
            print(i)
        if f==0 :
         print("ITEM ID NOT FOUND.")       
    elif choice == 8:
        break
    else:
        print("INVALID CHOICE. PLEASE TRY AGAIN.")     


