from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Sorting Algorithms Visualization')
root.geometry("900x700")
root.config(bg='black')

select_alg = StringVar()

def generate():
    print("Selected Algorithm" + select_alg.get())

UI_Frame = Frame(root,width=900,height=200,bg='grey')
UI_Frame.grid(row=0,column=0,padx=10,pady=5)

canvas = Canvas(root,width=900,height=500,bg='white')
canvas.grid(row=1,column=0,padx=10,pady=5)

Label(UI_Frame,text="Algorithm: " , bg="grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)
algMenu = ttk.Combobox(UI_Frame,textvariable=select_alg,values=['Bubble Sort','Merge Sort'])
algMenu.grid(row=0,column=1,padx=5,pady=5)
algMenu.current(0)

Button(UI_Frame,text="Generate",command=generate,bg='red').grid(row=0,column=2,padx=5,pady=5)


Label(UI_Frame,text="Size: " , bg="grey").grid(row=1,column=0,padx=5,pady=5,sticky=W)
sizeEntry = Entry(UI_Frame)
sizeEntry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

Label(UI_Frame,text="Min Value : " , bg="grey").grid(row=1,column=2,padx=5,pady=5,sticky=W)
minEntry = Entry(UI_Frame)
minEntry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

Label(UI_Frame,text="Max Value: " , bg="grey").grid(row=1,column=4,padx=5,pady=5,sticky=W)
maxEntry = Entry(UI_Frame)
maxEntry.grid(row=1,column=5,padx=5,pady=5,sticky=W)



root.mainloop()