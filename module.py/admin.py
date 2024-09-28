# emp= [{'id':100,'name':'name','age':20,'salary':10000,'place':'knr','dob':'30/12/2003','password':'30/12/2003'}]
emp=[]
def add_emp():
    id=str(input('enter your id: '))
    f1=0
    for i in emp:
        if i['id']==id:
            f1=1
            print('existing id')
            add_emp()
    if f1==0:
        name=(input('enter your name: '))
        age=int(input('enter your age: '))
        salary=int(input('enter your salary: '))
        place=(input('enter your place: '))
        dob=(input('enter your date of birth: '))
        password=dob
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob,'password':password})
        print('Employee added successfully')

def update():
    id=str(input('enter your id: '))
    f2=0
    for i in emp:
        if i['id']==id:
            f2=1
            name=(input('enter your name: '))
            age=int(input('enter your age: '))
            salary=int(input('enter your salary: '))
            place=(input('enter your place: '))
            dob=(input('enter your date of birth: '))
            i['name']=name
            i['age']=age
            i['salary']=salary
            i['place']=place
            i['date_of_birth']=dob
            print('updated successfully')
    if f2==0:
        print('invalid id')        

def delete():
    id=str(input('enter your id: '))
    f3=0
    for i in emp:
        if i['id']==id:
            f3=1
            emp.remove(i)
            print('REMOVED')
    if f3==0:
        print('invalid id')


def display():
    print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format('id','name','age','salary','place','dob'))
    print('_'*65)
    for i in emp:
            print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<15}".format(i['id'],i['name'],i['age'],i['salary'],i['place'],i['dob']))  
     

                              