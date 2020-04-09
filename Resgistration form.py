from tkinter import *
import cx_Oracle
root = Tk()
root.title("Registration Form")
root.geometry("350x500+500+120")
con = cx_Oracle.connect("system/admin@localhost:1521/xe")
cur = con.cursor()

def runserver():
    name = ename.get()
    mname = emname.get()
    fname = efname.get()
    dob = edob.get()
    addres = eaddress.get()
    pincode = ezipCode.get()
    depart = edeb.get()
    branch = ebranch.get()
    cont = econt.get()
    mail = email.get()
    stmt = 'insert into stdb(name,mother_name,father_name,dob,address,zip_code,department,branch,contact,email)values(\''+str(name)+'\',\''+str(mname)+'\',\''+str(fname)+'\',\''+str(dob)+'\',\''+str(addres)+'\',\''+str(pincode)+'\',\''+str(depart)+'\',\''+str(branch)+'\',\''+str(cont)+'\',\''+str(mail)+'\')'
    cur.execute(stmt)
    con.commit()
    print("mission successful")
name = Label(root,text=' Name')
name.place(x=10, y = 10)
ename = Entry(root)
ename.place(x=175,y=10)

mname = Label(root, text = "Mother's Name")
mname.place(x = 10, y = 45)
emname = Entry(root)
emname.place(x=175,y=45)

fname = Label(root, text = "Father's Name")
fname.place(x = 10, y = 80)
efname = Entry(root)
efname.place(x=175,y=80)

dob = Label(root, text="DOB")
dob.place(x=10, y=115)
edob = Entry(root)
edob.place(x=175, y=115)

address = Label(root, text='Address')
address.place(x=10, y=150)
eaddress = Entry(root)
eaddress.place(x=175, y=150)

zipCode = Label(root, text = "Zip Code")
zipCode.place(x=10, y = 185)
ezipCode = Entry(root)
ezipCode.place(x=175, y = 185)

deb = Label(root, text = 'Department')
deb.place(x = 10, y = 220)
edeb = Entry(root)
edeb.place(x=175, y = 220)

branch = Label(root,text = "Branch")
branch.place(x=10, y=255)
ebranch = Entry(root)
ebranch.place(x=175, y=255)

cont = Label(root,text = 'Contact No.')
cont.place(x = 10, y = 290)
econt= Entry(root)
econt.place(x = 175,  y = 290)

mail = Label(root, text = "E-Mail")
mail.place(x = 10, y = 325)
email = Entry(root)
email.place(x = 175, y = 325)
submit = Button(root, text = 'Submit',width = 7 , bd = 5, command = runserver)
submit.place(x=90, y = 370)
exitb = Button(root,text = "Exit", width = 7, bd =5, command = root.quit)
exitb.place(x=175, y = 370)

root.mainloop()