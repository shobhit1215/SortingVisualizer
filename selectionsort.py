import time

def selection_sort(data,drawData,speed):
    for i in range(len(data)):
        min_index=i
        colorArray = ['black' if x==i else 'red' for x in range(len(data))]
        drawData(data,colorArray)
        time.sleep(speed)
        for j in range(i+1,len(data)):
            if data[min_index]>data[j]:
                min_index = j
                colorArray = ['blue' if x==min_index or x==i else 'red' for x in range(len(data))]
                drawData(data,colorArray)
                time.sleep(speed)
        data[i],data[min_index]=data[min_index],data[i]
        drawData(data,['green' if x==i or x==min_index else 'red' for x in range(len(data))])
        time.sleep(speed)
    drawData(data,['green' for x in range(len(data))])
