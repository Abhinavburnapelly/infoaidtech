import tkinter.messagebox as mg;
from tkinter import *

global count
count=0

def submit():
    global count
    text1=text.get().capitalize()
    if(text1=='' or text1==' '):
        pass
    else:
        text.delete(0,'end')
        task_list.insert(count,"  "+text1)
        count+=1

def remove_all():
    task_list.delete(0,'end')

def delete():
    selected_checkboxs = task_list.curselection()
  
    for selected_checkbox in selected_checkboxs[::-1]:
        task_list.delete(selected_checkbox)

root=Tk()
root.title('To do list')
root.config(bg='#e2deff')
root.geometry("500x500")
root.resizable(False,False)



frame=Frame(root,bg='#118fee')
frame.pack(side=TOP)

label1=Label(frame,text='Enter a task',font="bold 15")
label1.pack(side=TOP,pady=10)

# text
text=Entry(frame,width=10,textvariable=StringVar(),font=('Arial 24'))
text.pack(side=LEFT,padx=10,pady=5)

submit_button=Button(frame,text='Submit',font="cosmicsms 15 normal",command=submit)
submit_button.pack(side=LEFT,padx=10,pady=5)

remove_allb=Button(frame,text='Clear',font="cosmicsms 15 normal",command=remove_all)
remove_allb.pack(side=LEFT,padx=10,pady=5)

delete_button=Button(frame,text='Delete',font="cosmicsms 15 normal",command=delete)
delete_button.pack(side=RIGHT,padx=10,pady=5)
# frame 2

frame2=Frame(root)
frame2.pack(side=TOP,pady=20)
task_list=Listbox(frame2,font=('arial 20'),selectmode=MULTIPLE)


task_list.pack(side=TOP)

root.mainloop()