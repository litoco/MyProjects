from tkinter import *
root1 = Tk()
root1.geometry('550x400')
#def dessert():
    
img = PhotoImage(file='image1.gif')
img2 = PhotoImage(file='image2.gif')
img3 = PhotoImage(file='image3.gif')
img4 = PhotoImage(file='image4.gif')
f1= Frame(root1,height=250,width=250,bg='green')
Checkbutton(f1,image=img).grid()
f1.grid()
f2= Frame(root1,height=250,width=250,bg='blue')
Checkbutton(f2,image=img2).grid()
f2.grid(row=0,column=1)
f3= Frame(root1,height=250,width=250,bg='yellow')
Checkbutton(f3,image=img3).grid()
f3.grid(row=1,column=0)
f4= Frame(root1,height=250,width=250,bg='red')
Checkbutton(f4,image=img4).grid()
f4.grid(row=1,column=1)
root1.mainloop()
#def f1():
#    dessert()

#f1()
