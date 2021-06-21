from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title('Sorting Algorithms Visualization')
root.geometry("900x700")
root.config(bg='black')

select_alg = StringVar()

def drawData(data):
    canvas.delete("all")
    c_height = 500
    c_width = 900
    x_width = c_width/(len(data)+1)
    offset= 30
    spacing=10
    normalizeddata = [i/max(data) for i in data]

    for i, height in enumerate(normalizeddata):
        x0=i*x_width +offset +spacing
        y0=c_height - height * 340

        x1=(i+1)*x_width + offset
        y1=c_height

        canvas.create_rectangle(x0,y0,x1,y1,fill="red")
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))



def generate():
    print("Selected Algorithm" + select_alg.get())
    try:
        minValue = int(minEntry.get())
    except:
        minValue = 1
    try:
        maxValue = int(maxEntry.get())
    except:
        maxValue =100
    try:
        size = int(sizeEntry.get())
    except:
        size =20
    if minValue<0 : minValue=0
    if maxValue > 1000 : maxValue=1000
    if size > 50 : size=50
    if size <3 :size=3
    if minValue > maxValue : minValue,maxValue=maxValue,minValue
    data = []
    for _ in range(size):
        data.append(random.randrange(minValue,maxValue+1))
    drawData(data)

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