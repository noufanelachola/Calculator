from tkinter import *

# Defining the window root
root = Tk()
root.title('Simple Calculator')

# Defining for the entry box
e = Entry(root,width=35,borderwidth=5)
e.grid(row = 0 , column = 0, columnspan=3 , padx=10 , pady=10)

# Defining  for number selection
def button_click(number) :
    current  = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))    

# Defining for clear button 
def button_clear() :
        e.delete(0,END)

# Defining for equal button
def button_equal():
    second_number = e.get()
    e.delete(0,END)      
   
    if funct == 'addition' :   
        e.insert(0, f_num + float(second_number))

    if funct == 'subtraction' :   
        e.insert(0, f_num - float(second_number))
    
    if funct == 'multiplication' :   
        e.insert(0, f_num * float(second_number))
    
    if funct == 'division' :   
        e.insert(0, f_num / float(second_number))

# Defining for add button
def button_add() :
    first_number = e.get()
    global f_num 
    global funct
    funct = 'addition'
    f_num = float(first_number)
    e.delete(0,END)        

# Defining for subtract button
def button_sub() :
    first_number = e.get()
    global f_num 
    global funct
    funct = 'subtraction'
    f_num = float(first_number)
    e.delete(0,END)     

# Defining for multiplication button
def button_mult() :
    first_number = e.get()
    global f_num 
    global funct
    funct = 'multiplication'
    f_num = float(first_number)
    e.delete(0,END)     

# Defining for division button
def button_div() :
    first_number = e.get()
    global f_num 
    global funct
    funct = 'division'
    f_num = float(first_number)
    e.delete(0,END)     


# Define buttons
but_1 = Button(root,text='1',padx=40,pady=20,command=lambda: button_click(1))
but_2 = Button(root,text='2',padx=40,pady=20,command=lambda: button_click(2))
but_3 = Button(root,text='3',padx=40,pady=20,command=lambda: button_click(3))

but_4 = Button(root,text='4',padx=40,pady=20,command=lambda: button_click(4))
but_5 = Button(root,text='5',padx=40,pady=20,command=lambda: button_click(5))
but_6 = Button(root,text='6',padx=40,pady=20,command=lambda: button_click(6))

but_7 = Button(root,text='7',padx=40,pady=20,command=lambda: button_click(7))
but_8 = Button(root,text='8',padx=40,pady=20,command=lambda: button_click(8))
but_9 = Button(root,text='9',padx=40,pady=20,command=lambda: button_click(9))

but_0 = Button(root,text='0',padx=40,pady=20,command=lambda: button_click(0))
but_add = Button(root,text='+',padx=39,pady=20,command=button_add)

but_equal = Button(root,text='=',padx=88,pady=20,command=button_equal)
but_clear = Button(root,text='Clear',padx=79,pady=20,command=button_clear)

but_sub = Button(root,text='-',padx=41,pady=20,command=button_sub)
but_mult = Button(root,text='x',padx=40,pady=20,command=button_mult)
but_div = Button(root,text='/',padx=41,pady=20,command=button_div)

# Pack buttons to the Window
but_1.grid(row=3,column=0)
but_2.grid(row=3,column=1)
but_3.grid(row=3,column=2)

but_4.grid(row=2,column=0)
but_5.grid(row=2,column=1)
but_6.grid(row=2,column=2)

but_7.grid(row=1,column=0)
but_8.grid(row=1,column=1)
but_9.grid(row=1,column=2)

but_0.grid(row=4,column=0)
but_equal.grid(row=4,column=1,columnspan=2)

but_add.grid(row=5,column=0)
but_clear.grid(row=5,column=1,columnspan=2)

but_sub.grid(row=6,column=0)
but_mult.grid(row=6,column=1)
but_div.grid(row=6,column=2)

root.mainloop()