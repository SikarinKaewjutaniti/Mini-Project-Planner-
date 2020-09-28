#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *

from tkcalendar import *

from tkinter import ttk

i= 0

window = Tk()


window.title("Pem Planner")
tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Time')

tab_control.add(tab2, text='To Do list')
cal= Calendar(tab1, selectmode = "day", year = 2020, month = 9, day = 27)
cal.pack(pady = 20)
cal.grid(column=0, row=0)

tree=ttk.Treeview(tab2)
tree["columns"]=("Date","Task", "Prioity")

tree.heading("Date",text="Date",anchor=W)
tree.heading("Task", text="Task",anchor=W)
tree.heading("Prioity", text="Prioity",anchor=W)


tree.column("Date", width=250, minwidth=270, stretch=NO)
tree.column("Task", width=500, minwidth=150, stretch=NO)
tree.column("Prioity", width=150, minwidth=200)
tree.pack()



tab_control.pack(expand=1, fill='both')

def plan():
    date = cal.get_date()
    tree.insert("" , "0" ,"Date", text = date)
    tree.pack()
    i+= 1
make_plan = Button(tab1, text = "make plan" , command = plan)
make_plan.grid(column=0, row=1)
window.geometry('1920x1080')

window.mainloop()


# In[ ]:





# In[ ]:




