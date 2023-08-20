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
root.geometry("500x560")
root.resizable(False,False)



frame=Frame(root,bg='#118fee',highlightbackground="blue", highlightthickness=2)
frame.pack(side=TOP,pady=5)
frame.configure(width=30)
label1=Label(frame,text='Enter a task',font="bold 15")
label1.pack(side=TOP,pady=10)

# text
text=Entry(frame,width=10,textvariable=StringVar(),font=('Arial 20'))
text.pack(side=LEFT,padx=10,pady=5)

submit_button=Button(frame,text='Submit',font="cosmicsms 15 normal",command=submit)
submit_button.pack(side=LEFT,padx=10,pady=5)



delete_button=Button(frame,text='Delete',font="cosmicsms 15 normal",command=delete)
delete_button.pack(side=RIGHT,padx=10,pady=5)
# frame 2

frame2=Frame(root,highlightbackground="grey", highlightthickness=3)
frame2.pack(side=TOP,pady=10)
task_list=Listbox(frame2,font=('cosmicsms 20'),selectmode=MULTIPLE)
task_list.configure(width=30,)
task_list.pack(side=TOP,fill=X, expand=YES)


# frame 3
frame3=Frame(root,highlightbackground="black", highlightthickness=1)

clear_img=PhotoImage(file='clear all.png')

remove_allb=Button(frame3,image=clear_img,font="cosmicsms 15 normal",command=remove_all)
remove_allb.pack(side=TOP,padx=10)
clear_all=Label(frame3,text='clear all',font="cosmicsms 10 normal")
clear_all.pack(side=BOTTOM,pady=5)

frame3.pack(side=TOP)

root.mainloop()
