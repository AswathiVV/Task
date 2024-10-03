from admin import emp 
def login():
    uname=input('ener your user name: ')
    passwrd=input('ener your password: ')
    f=0
    user=''
    if uname=='admin' and passwrd=='admin':
        f=1
    for i in emp:
        if i['id']==uname and i['password']==passwrd:
            f=2
            user=i
    return f,user             