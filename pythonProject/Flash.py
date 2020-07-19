from tkinter import *
r1 = Tk()
r1.configure(background='black')
def des():
    r1.destroy()
    import pro
Label(r1,text="Project On Restaurant Billing ",fg='white',bg='black',font='helvetica 40 bold').grid(columnspan=2)
Label(r1,text="Developed By : Ashutosh Kumar ",fg='white',bg='black',font='helvetica 10 bold',anchor='center').grid(row=1,columnspan=2)
Label(r1,text="Mobile Number : 8369704271",fg='white',bg='black',font='helvetica 10 bold',anchor='w').grid(row=2,column=0,sticky='w')
Label(r1,text="Email Id : ashutoshkr.1907@gmail.com",bg='black',fg='white',font='helvetica 10 bold',anchor='e').grid(row=2,column=1,sticky='e')
r1.after('5000',des)
r1.mainloop()
