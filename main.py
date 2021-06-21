
#Packages
from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort
from selectionsort import selection_sort

#Tkinter object
root = Tk()
root.title('Sorting Algorithms Visualization')
root.geometry('1000x700+200+50')
root.config(bg='black')
root.resizable(False,False)

#variables
select_alg = StringVar()
data = []

#Functions
#To draw the array
def drawData(data,colorArray):
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

        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))

    root.update_idletasks()


#Generate random array in every call
def generate():
    global data
  
    minValue = int(minEntry.get())
    maxValue = int(maxEntry.get())
    size = int(sizeEntry.get())
    data = []
    for _ in range(size):
        data.append(random.randrange(minValue,maxValue+1))
    drawData(data,['red' for x in range(len(data))])

#Calls the particular algorithm
def startAlgorithm():
    global data
    alg = algMenu.get()
    if alg=='Selection Sort':
        selection_sort(data,drawData,speedScale.get())
    if alg=='Bubble Sort':
        bubble_sort(data,drawData,speedScale.get())

#GUI application

UI_Frame = Frame(root,width=950,height=200,bg='grey')
UI_Frame.grid(row=0,column=0,padx=10,pady=5)

canvas = Canvas(root,width=950,height=500,bg='white')
canvas.grid(row=1,column=0,padx=10,pady=5)

Label(UI_Frame,text="Algorithm: " , bg="grey").grid(row=0,column=0,padx=5,pady=5,sticky=W)
algMenu = ttk.Combobox(UI_Frame,textvariable=select_alg,values=['Bubble Sort','Selection Sort'])
algMenu.grid(row=0,column=1,padx=5,pady=5)


speedScale = Scale(UI_Frame, from_=0.1 ,to=2.0,length = 200,digits=2,resolution=0.2,orient=HORIZONTAL,label="Select Speed[s]")
speedScale.grid(row=0,column=2,padx=5,pady=5)


Button(UI_Frame,text="Start",command=startAlgorithm,bg='red',relief=GROOVE).grid(row=0,column=3,padx=5,pady=5)



sizeEntry = Scale(UI_Frame,from_=3,to=50,resolution=1,orient=HORIZONTAL,label="Array Size")
sizeEntry.grid(row=1,column=0,padx=5,pady=5)


minEntry = Scale(UI_Frame,from_=1,to=100,resolution=1,orient=HORIZONTAL,label="Min Value")
minEntry.grid(row=1,column=1,padx=5,pady=5)


maxEntry = Scale(UI_Frame,from_=100,to=1000,resolution=1,orient=HORIZONTAL,label="Max Value")
maxEntry.grid(row=1,column=2,padx=5,pady=5)


Button(UI_Frame,text="Generate",command=generate,bg='white',relief=GROOVE).grid(row=1,column=3,padx=5,pady=5)


root.mainloop()