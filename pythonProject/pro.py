from tkinter import *
from tkinter.messagebox import *
from database import *
root = Tk()
root.geometry('1260x660')
root.title("RESTRAUNT ORDER")
veG=burgeR=rollS=drinkS=nonveG=0
v00 = IntVar()
v01 = IntVar()
v10 = IntVar()
v11 = IntVar()
v20 = IntVar()
v21 = IntVar()
v04 = IntVar()
v05 = IntVar()
v14 = IntVar()
v15 = IntVar()
v24 = IntVar()
v25 = IntVar()
v06 = IntVar()
v07 = IntVar()
v16 = IntVar()
v17 = IntVar()
v26 = IntVar()
v27 = IntVar()
t= StringVar()

c=0
mit=[]
allinfo=[]
price=0
prev=''
def add(s):
    global price,prev
    c=0
    string = s.split(",")
    
    for i in mit:
        if(string[0]==i):
            price -= int(string[1])
            mit.remove(i)
            c=1
    if(c==0 and(v00.get()!=0 or v01.get()!=0 or v10.get()!=0 or v11.get()!=0 or v20.get()!=0 or v21.get()!=0 or v04.get()!=0 or v05.get()!=0 or v14.get()!=0 or v15.get()!=0 or v24.get()!=0 or v25.get()!=0 or v06.get()!=0 or v07.get()!=0 or v16.get()!=0 or v17.get()!=0 or v26.get()!=0 or v27.get()!=0)):
        prev = string[0]
        mit.append(string[0])
        price += int(string[1])
    t.set('Total: '+str(price))
    #mit=[]
    
def clrscr():
    def work():
        r.destroy()
    name.delete(0,END)
    mno.delete(0,END)
    add1.delete(0,END)
    add2.delete(0,END)
    add3.delete(0,END)
    r =Toplevel()
    r.title("Quantity details")
    label1 = Label(r,height=13,width=15)
    s = Scrollbar(label1)
    s.pack(side=RIGHT, fill=Y)
    l = Listbox(label1,height=13,width=31)
    l.pack()
    l.config(yscrollcommand=s.set)
    s.config(command=l.yview)
    label1.grid(row=0,column=0)
    label2 = Label(r,height=13,width=15)
    Button(label2,text='OK',command=work,height=2,width=28).pack()
    label2.grid(row=1,column=0)
    b=fetch(mit)
    print(b)
    l.insert(END, "SLNO   Name")
    for i in b:
        l.insert(END,str(i[0])+'   '+i[1])
    r.mainloop()
    

def insertinto():
    allinfo =[]
    global c,price
    c+=1
    if(name.get() and len(mno.get())==10 and add1.get() and add2.get() and add3.get()):
        if(price!=0):
            t.set('Please Pay '+str(price))
        allinfo.append(name.get())
        allinfo.append(mno.get())
        allinfo.append(add1.get()+','+add2.get()+','+add3.get())
        insert(mit)
        insertall(allinfo)
##        b=fetch()
        
        a = fetchall()
        for i in a[0] :
            listbox.insert(END, i)
        listbox.insert(END,'')
        
    else:
        showerror('Error','Please Enter Your Name\n\n10 digit Mob.No. and \n\nCorrect and Full Address')

def vegfun():
    #newmenuitem_initialise(7)
    newmenuitem=Frame(menuitem,height=100,width=1240,bg='lawngreen',relief='solid')
    newmenuitem.grid(row=1,columnspan=3)
    global veG,burgeR,rollS,drinkS,nonveG
    veG+=1
    if(veG%2!=0):
        burger.configure(bg='OliveDrab1')
        nonveg.configure(bg='OliveDrab1')
        rolls.configure(bg='OliveDrab1')
        drinks.configure(bg='OliveDrab1')
        veg.configure(bg='OliveDrab4')
        burgeR=rollS=drinkS=nonveG=0
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen').grid(row=0,column=0)
        Label(newmenuitem,text='Price(F/H)',font='times 12 bold',bg='lawngreen').grid(row=0,column=1,columnspan=2)
        Label(newmenuitem,text='Chapati',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=0)
        Checkbutton(newmenuitem,text='5(Simple)',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v00,onvalue=1,command=lambda:add('Simple Chapati,5')).grid(row=1,column=1)
        Checkbutton(newmenuitem,text='10(Butter)',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v01,onvalue=1,command=lambda:add('Butter Chapati,10')).grid(row=1,column=2)
        Label(newmenuitem,text='Kadai Paneer',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=0)
        Checkbutton(newmenuitem,text='200',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v10,onvalue=1,command=lambda:add('Full Kadai Paneer,200')).grid(row=2,column=1)
        Checkbutton(newmenuitem,text='110',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v11,onvalue=1,command=lambda:add('Half Kadai Paneer,110')).grid(row=2,column=2)
        Label(newmenuitem,text='Paneer Butter Masala',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=0)
        Checkbutton(newmenuitem,text='230',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v20,onvalue=1,command=lambda:add('Full Paneer Butter Masala,230')).grid(row=3,column=1)
        Checkbutton(newmenuitem,text='125',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v21,onvalue=1,command=lambda:add('Half Paneer Butter Masala,125')).grid(row=3,column=2)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen').grid(row=0,column=3)
        Label(newmenuitem,text='Price(F/H)',font='times 12 bold',bg='lawngreen').grid(row=0,column=4,columnspan=2)
        Label(newmenuitem,text='Pulao Tadka',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=3)
        Checkbutton(newmenuitem,text='250',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v04,onvalue=1,command=lambda:add('Full Pulao Tadka,250')).grid(row=1,column=4)
        Checkbutton(newmenuitem,text='135',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v05,onvalue=1,command=lambda:add('Half Pulao Tadka,135')).grid(row=1,column=5)
        Label(newmenuitem,text='Fried Rice',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=3)
        Checkbutton(newmenuitem,text='180',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v14,onvalue=1,command=lambda:add('Full Fried Rice,180')).grid(row=2,column=4)
        Checkbutton(newmenuitem,text='100',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v15,onvalue=1,command=lambda:add('Half Fried Rice,100')).grid(row=2,column=5)
        Label(newmenuitem,text='Veg Biryani',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=3)
        Checkbutton(newmenuitem,text='300',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v24,onvalue=1,command=lambda:add('Full Veg Biryani,300')).grid(row=3,column=4)
        Checkbutton(newmenuitem,text='160',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v25,onvalue=1,command=lambda:add('Half Veg Biryani,160')).grid(row=3,column=5)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen').grid(row=0,column=6)
        Label(newmenuitem,text='Price(F/H)',font='times 12 bold',bg='lawngreen').grid(row=0,column=7,columnspan=2)
        Label(newmenuitem,text='Shahi Paneer',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=6)
        Checkbutton(newmenuitem,text='260',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v06,onvalue=1,command=lambda:add('Full Shahi Paneer,260')).grid(row=1,column=7)
        Checkbutton(newmenuitem,text='140',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v07,onvalue=1,command=lambda:add('Half Shahi Paneer,140')).grid(row=1,column=8)
        Label(newmenuitem,text='Mutter Paneer',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=6)
        Checkbutton(newmenuitem,text='120',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v16,onvalue=1,command=lambda:add('Full Mutter Paneer,120')).grid(row=2,column=7)
        Checkbutton(newmenuitem,text='70',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v17,onvalue=1,command=lambda:add('Half Mutter Paneer,70')).grid(row=2,column=8)
        Label(newmenuitem,text='Paneer Masala',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=6)
        Checkbutton(newmenuitem,text='230',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v26,onvalue=1,command=lambda:add('Full Paneer Masala,230')).grid(row=3,column=7)
        Checkbutton(newmenuitem,text='125',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v27,onvalue=1,command=lambda:add('Half Paneer Masala,125')).grid(row=3,column=8)       
    else:
        veg.configure(bg='OliveDrab1')
        

def nonvegfun():
    #newmenuitem_initialise(7)
    newmenuitem=Frame(menuitem,height=100,width=1240,bg='lawngreen',relief='solid')
    newmenuitem.grid(row=1,columnspan=3)
    global veG,burgeR,rollS,drinkS,nonveG
    nonveG += 1
    if(nonveG%2!=0):
        burger.configure(bg='OliveDrab1')
        nonveg.configure(bg='OliveDrab4')
        rolls.configure(bg='OliveDrab1')
        drinks.configure(bg='OliveDrab1')
        veg.configure(bg='OliveDrab1')
        veG=burgeR=rollS=drinkS=0
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen').grid(row=0,column=0)
        Label(newmenuitem,text='Price(F/H)',font='times 12 bold',bg='lawngreen').grid(row=0,column=1,columnspan=2)
        Label(newmenuitem,text='Chicken Biryani',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=0)
        Checkbutton(newmenuitem,text='220',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v00,onvalue=2,command=lambda:add('Full Chicken Biryani,220')).grid(row=1,column=1)
        Checkbutton(newmenuitem,text='130',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v01,onvalue=2,command=lambda:add('Half Chicken Biryani,130')).grid(row=1,column=2)
        Label(newmenuitem,text='Chicken Kabab',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=0)
        Checkbutton(newmenuitem,text='200',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v10,onvalue=2,command=lambda:add('Full Chicken Kabab,200')).grid(row=2,column=1)
        Checkbutton(newmenuitem,text='110',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v11,onvalue=2,command=lambda:add('Half Chicken Kabab,110')).grid(row=2,column=2)
        Label(newmenuitem,text='Chicken Boneless',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=0)
        Checkbutton(newmenuitem,text='230',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v20,onvalue=2,command=lambda:add('Full Chicken Boneless,230')).grid(row=3,column=1)
        Checkbutton(newmenuitem,text='125',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v21,onvalue=2,command=lambda:add('Half Chicken Boneless,125')).grid(row=3,column=2)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen').grid(row=0,column=3)
        Label(newmenuitem,text='Price(F/H)',font='times 12 bold',bg='lawngreen').grid(row=0,column=4,columnspan=2)
        Label(newmenuitem,text='Butter Chicken',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=3)
        Checkbutton(newmenuitem,text='250',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v04,onvalue=2,command=lambda:add('Full Butter Chicken,250')).grid(row=1,column=4)
        Checkbutton(newmenuitem,text='135',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v05,onvalue=2,command=lambda:add('Half Butter Chicken,135')).grid(row=1,column=5)
        Label(newmenuitem,text='Tandoori Chicken',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=3)
        Checkbutton(newmenuitem,text='180',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v14,onvalue=2,command=lambda:add('Full Tandoori Chicken,180')).grid(row=2,column=4)
        Checkbutton(newmenuitem,text='100',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v15,onvalue=2,command=lambda:add('Half Tandoori Chicken,100')).grid(row=2,column=5)
        Label(newmenuitem,text='Haandi Chicken',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=3)
        Checkbutton(newmenuitem,text='300',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v24,onvalue=2,command=lambda:add('Full Haandi Chicken,300')).grid(row=3,column=4)
        Checkbutton(newmenuitem,text='160',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v25,onvalue=2,command=lambda:add('Half Haandi Chicken,160')).grid(row=3,column=5)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen').grid(row=0,column=6)
        Label(newmenuitem,text='Price(F/H)',font='times 12 bold',bg='lawngreen').grid(row=0,column=7,columnspan=2)
        Label(newmenuitem,text='Chicken 69',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=6)
        Checkbutton(newmenuitem,text='260',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v06,onvalue=2,command=lambda:add('Full Chicken 69,260')).grid(row=1,column=7)
        Checkbutton(newmenuitem,text='140',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v07,onvalue=2,command=lambda:add('Full Chicken 69,140')).grid(row=1,column=8)
        Label(newmenuitem,text='Fish Fry',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=6)
        Checkbutton(newmenuitem,text='120',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v16,onvalue=2,command=lambda:add('Full Fish Fry,120')).grid(row=2,column=7)
        Checkbutton(newmenuitem,text='70',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v17,onvalue=2,command=lambda:add('Half Fish Fry,70')).grid(row=2,column=8)
        Label(newmenuitem,text='Spicy Roasted Chicken',width=20,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=6)
        Checkbutton(newmenuitem,text='230',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v26,onvalue=2,command=lambda:add('Full Spicy Roasted Chicken,230')).grid(row=3,column=7)
        Checkbutton(newmenuitem,text='125',width=10,font='times 10 bold',bg='lawngreen',anchor='w',variable=v27,onvalue=2,command=lambda:add('Half Spicy Roasted Chicken,125')).grid(row=3,column=8)
    else:
        nonveg.configure(bg='OliveDrab1')
def burgersfun():
    global veG,burgeR,rollS,drinkS,nonveG
    #newmenuitem_initialise(7)
    newmenuitem=Frame(menuitem,height=100,width=1240,bg='lawngreen',relief='solid')
    newmenuitem.grid(row=1,columnspan=3)
    burgeR += 1
    if(burgeR%2!=0):
        burger.configure(bg='OliveDrab4')
        nonveg.configure(bg='OliveDrab1')
        rolls.configure(bg='OliveDrab1')
        drinks.configure(bg='OliveDrab1')
        veg.configure(bg='OliveDrab1')
        veG=rollS=drinkS=nonveG=0
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=0)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=1,columnspan=2,sticky='w')
        Label(newmenuitem,text='Chicken Burger',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=0)
        Checkbutton(newmenuitem,text='80',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v00,onvalue=3,command=lambda:add('Chicken Burger,80')).grid(row=1,column=1)
        Label(newmenuitem,text='Cheese Burger',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=0)
        Checkbutton(newmenuitem,text='60',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v10,onvalue=3,command=lambda:add('Cheese Burger,60')).grid(row=2,column=1)
        Label(newmenuitem,text='Zinger Burger',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=0)
        Checkbutton(newmenuitem,text='70',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v20,onvalue=3,command=lambda:add('Zinger Burger,70')).grid(row=3,column=1)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=3)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=4,columnspan=2,sticky='w')
        Label(newmenuitem,text='Snacker',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=3)
        Checkbutton(newmenuitem,text='120',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v04,onvalue=3,command=lambda:add('Snacker,120')).grid(row=1,column=4)
        Label(newmenuitem,text='Potato Krisper',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=3)
        Checkbutton(newmenuitem,text='30',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v14,onvalue=3,command=lambda:add('Potato Krisper,30')).grid(row=2,column=4)
        Label(newmenuitem,text='Chicken Zinger',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=3)
        Checkbutton(newmenuitem,text='120',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v24,onvalue=3,command=lambda:add('Chicken Zinger,120')).grid(row=3,column=4)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=6)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=7,columnspan=2,sticky='w')
        Label(newmenuitem,text='Cream Burger',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=6)
        Checkbutton(newmenuitem,text='100',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v06,onvalue=3,command=lambda:add('Cream Burger,100')).grid(row=1,column=7)
        Label(newmenuitem,text='Maharaja Burger',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=6)
        Checkbutton(newmenuitem,text='150',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v16,onvalue=3,command=lambda:add('Maharaja Burger,150')).grid(row=2,column=7)
        Label(newmenuitem,text='Bacon Burger',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=6)
        Checkbutton(newmenuitem,text='80',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v26,onvalue=3,command=lambda:add('Bacon Burger,80')).grid(row=3,column=7)
    else:
        burger.configure(bg='OliveDrab1')

def rollsfun():
    global veG,burgeR,rollS,drinkS,nonveG
    #newmenuitem_initialise(7)
    newmenuitem=Frame(menuitem,height=100,width=1240,bg='lawngreen',relief='solid')
    newmenuitem.grid(row=1,columnspan=3)
    rollS += 1
    if(rollS%2!=0):
        burger.configure(bg='OliveDrab1')
        nonveg.configure(bg='OliveDrab1')
        rolls.configure(bg='OliveDrab4')
        drinks.configure(bg='OliveDrab1')
        veg.configure(bg='OliveDrab1')
        veG=burgeR=drinkS=nonveG=0
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=0)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=1,columnspan=2,sticky='w')
        Label(newmenuitem,text='Simple Veg Roll',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=0)
        Checkbutton(newmenuitem,text='30',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v00,onvalue=4,command=lambda:add('Simple Veg Roll,30')).grid(row=1,column=1)
        Label(newmenuitem,text='Cheese Roll',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=0)
        Checkbutton(newmenuitem,text='40',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v10,onvalue=4,command=lambda:add('Cheese Roll,40')).grid(row=2,column=1)
        Label(newmenuitem,text='Paneer Roll',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=0)
        Checkbutton(newmenuitem,text='60',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v20,onvalue=4,command=lambda:add('Paneer Roll,60')).grid(row=3,column=1)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=3)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=4,columnspan=2,sticky='w')
        Label(newmenuitem,text='Egg Roll',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=3)
        Checkbutton(newmenuitem,text='45',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v04,onvalue=4,command=lambda:add('Egg Roll,45')).grid(row=1,column=4)
        Label(newmenuitem,text='Egg Roll(Double Egg)',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=3)
        Checkbutton(newmenuitem,text='60',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v14,onvalue=4,command=lambda:add('Egg Roll(Double Egg),60')).grid(row=2,column=4)
        Label(newmenuitem,text='Manchurian Egg Roll',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=3)
        Checkbutton(newmenuitem,text='80',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v24,onvalue=4,command=lambda:add('Manchurian Egg Roll,80')).grid(row=3,column=4)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=6)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=7,columnspan=2,sticky='w')
        Label(newmenuitem,text='Cream Roll',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=6)
        Checkbutton(newmenuitem,text='50',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v06,onvalue=4,command=lambda:add('Cream Roll,50')).grid(row=1,column=7)
        Label(newmenuitem,text='Manchurian Veg Roll',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=6)
        Checkbutton(newmenuitem,text='60',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v16,onvalue=4,command=lambda:add('Manchurian Veg Roll,60')).grid(row=2,column=7)
        Label(newmenuitem,text='Special Roll',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=6)
        Checkbutton(newmenuitem,text='100',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v26,onvalue=4,command=lambda:add('Special Roll,100')).grid(row=3,column=7)
    else:
        rolls.configure(bg='OliveDrab1')

def drinksfun():
    global veG,burgeR,rollS,drinkS,nonveG
    #newmenuitem_initialise(7)
    newmenuitem=Frame(menuitem,height=100,width=1240,bg='lawngreen',relief='solid')
    newmenuitem.grid(row=1,columnspan=3)
    drinkS += 1
    if(drinkS%2!=0):
        burger.configure(bg='OliveDrab1')
        nonveg.configure(bg='OliveDrab1')
        rolls.configure(bg='OliveDrab1')
        drinks.configure(bg='OliveDrab4')
        veg.configure(bg='OliveDrab1')
        veG=burgeR=rollS=nonveG=0
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=0)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=1,columnspan=2,sticky='w')
        Label(newmenuitem,text='Coca Cola(150 ml)',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=0)
        Checkbutton(newmenuitem,text='40',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v00,onvalue=5,command=lambda:add('Coca Cola(150 ml),40')).grid(row=1,column=1)
        Label(newmenuitem,text='Milk Shake',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=0)
        Checkbutton(newmenuitem,text='40',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v10,onvalue=5,command=lambda:add('Milk Shake,40')).grid(row=2,column=1)
        Label(newmenuitem,text='Chruchy Choco Shake',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=0)
        Checkbutton(newmenuitem,text='60',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v20,onvalue=5,command=lambda:add('Chruchy Choco Shake,60')).grid(row=3,column=1)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=3)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=4,columnspan=2,sticky='w')
        Label(newmenuitem,text='Cold Coffee',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=3)
        Checkbutton(newmenuitem,text='50',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v04,onvalue=5,command=lambda:add('Cold Coffee,50')).grid(row=1,column=4)
        Label(newmenuitem,text='Mango Shake ',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=3)
        Checkbutton(newmenuitem,text='40',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v14,onvalue=5,command=lambda:add('Mango Shake,40')).grid(row=2,column=4)
        Label(newmenuitem,text='Hot Coffee',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=3)
        Checkbutton(newmenuitem,text='20',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v24,onvalue=5,command=lambda:add('Hot Coffee,20')).grid(row=3,column=4)
        Label(newmenuitem,text='Menu',width=20,font='times 12 bold',bg='lawngreen',anchor='w').grid(row=0,column=6)
        Label(newmenuitem,text='Price',font='times 12 bold',bg='lawngreen').grid(row=0,column=7,columnspan=2,sticky='w')
        Label(newmenuitem,text='Lassi',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=1,column=6)
        Checkbutton(newmenuitem,text='20',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v06,onvalue=5,command=lambda:add('Lassi,20')).grid(row=1,column=7)
        Label(newmenuitem,text='Lemonade',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=2,column=6)
        Checkbutton(newmenuitem,text='30',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v16,onvalue=5,command=lambda:add('Lemonade,30')).grid(row=2,column=7)
        Label(newmenuitem,text='Smoothy',width=30,font='times 10 bold',bg='lawngreen',anchor='w').grid(row=3,column=6)
        Checkbutton(newmenuitem,text='60',width=20,font='times 10 bold',bg='lawngreen',anchor='w',variable=v26,onvalue=5,command=lambda:add('Smoothy,60')).grid(row=3,column=7)
    else:
        drinks.configure(bg='OliveDrab1')

#frametop_title(1)
title = Frame(root,height=100,width=1256,borderwidth=10,relief='raise',bg='green2')
title.grid(columnspan=3)
#sidebar_initialised(2)
sidebar = Frame(root,height=350,width=120,borderwidth=8,relief='sunken',bg='lightcyan')
sidebar.grid(row=1,column=0,rowspan=2)
#details_initialise(3)
details=Frame(root,height=300,width=600,borderwidth=8,relief='sunken')
details.grid(row=1,column=1)
#menuFrame_initialised(4)
menu = Frame(root,height=50,width=898,borderwidth=8,relief='groove',bg='OliveDrab1')
menu.grid(row=2,column=1)
#offers_initialise(5)
offers=Frame(root,height=350,width=220,borderwidth=8,relief='sunken',bg='lightcyan')
offers.grid(row=1,column=2,rowspan=2)
#menuitem_initialise(6)
menuitem=Frame(root,height=154,width=1260,borderwidth=8,relief='groove',bg='lawngreen')
menuitem.grid(row=3,columnspan=3)
#newmenuitem_initialise(7)
newmenuitem=Frame(menuitem,height=100,width=1240,bg='lawngreen',relief='solid')
newmenuitem.grid(row=1,columnspan=3)
#total(8)
total=Frame(menuitem,height=23,width=1240,bg='purple',relief='solid')
total.grid(row=2,columnspan=3)
up = Frame(offers,height=40,width=210,bg='lightcyan')
up.grid()
do = Frame(offers,height=260,width=210,bg='lightcyan')
do.grid(row=1)
do2 = Frame(offers,height=40,width=210,bg='lightcyan')
do2.grid(row=2)
Label(up,text='Order Status',font='times 20 bold',bg='lightcyan').grid(columnspan=2)
do = Frame(offers,height=300,width=210,bg='lightcyan')
do.grid(row=1)
do2 = Frame(offers,height=40,width=210,bg='lightcyan')
do2.grid(row=2)
scrollbar = Scrollbar(do)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(do,height=15,width=31)
listbox.pack()
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
Button(do2,height=2,width=26,text='Print',command=lambda:clrscr(),bd=5).pack()
#initialisation_done

#1(
#inside_frametop_title
Label(title,text='HOT MEAL\'S',font='arial 50 bold',width=30,bg='green2').pack()
Label(title,text='A Family Restauraunt\t\t\t\tPhone:8034563423',font='arial 15 bold',bg='green2').pack(side='right')
#1)

#inside_sidebar 2(
def desert():
    root1=Toplevel()
    def do():
        root1.destroy()
    img = PhotoImage(file='image1.gif')
    img2 = PhotoImage(file='image2.gif')
    img3 = PhotoImage(file='image3.gif')
    img4 = PhotoImage(file='image4.gif')
    f1= Frame(root1,height=250,width=250,bg='green')
    Checkbutton(f1,image=img,variable=v00,onvalue=10,command=lambda:add('Dessert1,60')).grid()
    f1.grid()
    f2= Frame(root1,height=250,width=250,bg='green')
    Checkbutton(f2,image=img2,variable=v01,onvalue=10,command=lambda:add('Dessert2,60')).grid()
    f2.grid(row=0,column=1)
    f3= Frame(root1,height=250,width=250,bg='green')
    Checkbutton(f3,image=img3,variable=v10,onvalue=10,command=lambda:add('Dessert3,60')).grid()
    f3.grid(row=1,column=0)
    f4= Frame(root1,height=250,width=250,bg='green')
    Checkbutton(f4,image=img4,variable=v11,onvalue=10,command=lambda:add('Dessert4,60')).grid()
    f4.grid(row=1,column=1)
    Button(root1,text='OK',command=do).grid(row=2,column=1,sticky='e')
    root1.mainloop()

b1 = Button(sidebar,text='Dessert',font='system 10 bold',height=3,width=12,bg='lightcyan',bd=5,command=lambda:desert())
b1.grid()
b2 = Button(sidebar,text='Offers',font='system 10 bold',height=3,width=12,bg='lightcyan',bd=5)
b2.grid(row=1)
b3 = Button(sidebar,text='Popular Now',font='system 10 bold',height=3,width=12,bg='lightcyan',bd=5)
b3.grid(row=2)
b4 = Button(sidebar,text='Order Status',font='system 10 bold',height=3,width=12,bg='lightcyan',bd=5)
b4.grid(row=3)
b5 = Button(sidebar,text='Other\nBranches',font='system 10 bold',height=3,width=12,bg='lightcyan',bd=5)
b5.grid(row=4)
#2)

#inside_details 3(
info = Frame(details,height=284,width=880,borderwidth=8,bg='azure')
info.grid(row=1)
Label(info,text='FULL NAME:',font='times 15 bold',width='30',height='2',bg='azure',anchor='e').grid()
Label(info,text='MOBILE NUMBER:',font='times 15 bold',width='30',height='2',bg='azure',anchor='e').grid(row=1)
Label(info,text='ADDRESS(HOUSE_NO./STREET):',font='times 15 bold',height='2',width='30',bg='azure',anchor='e').grid(row=2)
Label(info,text='ADDRESS(LOCALITY):',font='times 15 bold',width='30',height='2',bg='azure',anchor='e').grid(row=3)
Label(info,text='ADDRESS(CITY):',font='times 15 bold',width='30',height='2',bg='azure',anchor='e').grid(row=4)

name = Entry(info,width=30,font='times 15 bold')
name.grid(row=0,column=1,sticky='w',padx=33)
mno = Entry(info,width=30,font='times 15 bold')
mno.grid(row=1,column=1,sticky='w',padx=33)
add1 = Entry(info,width=43,font='times 15 bold')
add1.grid(row=2,column=1,padx=33)
add2 = Entry(info,width=43,font='times 15 bold')
add2.grid(row=3,column=1,padx=33)
add3 = Entry(info,width=43,font='times 15 bold')
add3.grid(row=4,column=1,padx=33)
#3)

#inside_menuFrame 4(
veg = Button(menu,text='Vegetarian',font='arial 13 bold',bd=10,width=15,bg='OliveDrab1',activebackground='OliveDrab4',command=vegfun)
veg.grid()
nonveg = Button(menu,text='Non-Vegetarian',font='arial 13 bold',bd=10,width=15,bg='OliveDrab1',activebackground='OliveDrab4',command=nonvegfun)
nonveg.grid(row=0,column=1)
burger = Button(menu,text='Burgers',font='arial 13 bold',bd=10,width=15,bg='OliveDrab1',activebackground='OliveDrab4',command=burgersfun)
burger.grid(row=0,column=2)
rolls = Button(menu,text='Rolls',font='arial 13 bold',bd=10,width=15,bg='OliveDrab1',activebackground='OliveDrab4',command=rollsfun)
rolls.grid(row=0,column=3)
drinks = Button(menu,text='Drinks',font='arial 13 bold',bd=10,width=15,bg='OliveDrab1',activebackground='OliveDrab4',command=drinksfun)
drinks.grid(row=0,column=4)
#4)

#inside_total 8(
Label(total,textvariable=t,font='arial 13 bold',bg='purple',width=113,anchor='e').grid()
t.set('Place Your Order Then Click Proceed')
Button(total,text='Proceed',font='arial 13 bold',width=9,bg='purple',bd=5,command=lambda:insertinto()).grid(row=0,column=1)
root.mainloop()
