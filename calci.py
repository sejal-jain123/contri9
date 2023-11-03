from tkinter import *
import math as m

def click(value):
    ex = entryfield.get()
    ans= ''

    try:

        if value =='C':
            ex= ex[0:len(ex)-1]
            entryfield.delete(0, END)
            entryfield.insert(0,ex)
            return 

        elif value == 'CE':
            entryfield.delete(0,END)

        elif value== 'sqrt':
            ans = m.sqrt(eval(ex))

        elif value=='pi':
            ans= m.pi

        elif value=='cos':
            ans= m.cos(m.radians(eval(ex)))

        elif value=='sin':
            ans= m.sin(m.radians(eval(ex)))

        elif value=='tan':
            ans= m.tan(m.radians(eval(ex)))

        elif value=='2pi':
            ans= 2*m.pi

        elif value=='cosh':
            ans= m.cosh(eval(ex))

        elif value=='sinh':
            ans= m.sinh(eval(ex))

        elif value=='tanh':
            ans= m.tanh(eval(ex))

        elif value== chr(8731):
            ans= eval(ex)**(1/3)

        elif value=='x\u02b8':
            entryfield.insert(END,'**')
            return

        elif value=='x\u00B3':
            ans= eval(ex)**3
        
        elif value=='x\u00B2':
            ans= eval(ex)**2

        elif value=='ln':
            ans= m.log2(eval(ex))

        elif value=='deg':
            ans= m.degrees(eval(ex))

        elif value=='rad':
            ans= m.radians(eval(ex))

        elif value=='e':
            ans= m.e

        elif value=='log':
            ans= m.log10(eval(ex))
        
        elif value=='x!':
            ans= m.factorial(ex)

        elif value== chr(247):
            entryfield.insert(END,"/")
            return

        elif value=='=':
            ans= eval(ex)

        else:
            entryfield.insert(END, value)

        entryfield.delete(0, END)
        entryfield.insert(0,ans)

    except SyntaxError:
        pass
    


root = Tk()
root.title("Scientific Calculator")
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

entryfield = Entry(root, font=('arial', 20, 'bold'),bg='dodgerblue3', fg='white', bd= 10,relief=SUNKEN, width=30)
entryfield.grid(row=0, column=0, columnspan=8)

button_text_list = ["C", "CE", "sqrt","+","pi", "cos","tan","sin",
                     "1","2","3","-", "2pi","cosh","tanh", "sinh",
                     "4","5","6","*",chr(8731), "x\u02b8","x\u00B3","x\u00B2",
                     "7","8","9","chr(247)","ln", "deg","rad", "e",
                     "0",".","%","=","log","","","x!"]

rowvalue=1
columnvalue=0
for i in button_text_list:

    button= Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white', font=('arial',18,'bold'), activebackground='dodgerblue3', command= lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue,pady=1)
    columnvalue +=1
    if columnvalue > 7:
        rowvalue +=1
        columnvalue =0



root.mainloop()