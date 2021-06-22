import time

def insertion_sort(data,drawData,speed):
    for i in range(1,len(data)):
        key = data[i]
        drawData(data,['black' if x==i else 'red' for x in range(len(data))])
        time.sleep(speed)
        j=i-1
        while j>=0 and key < data[j]:
            data[j+1]=data[j]
            drawData(data,['green' if x==j or x==j+1 else 'red' for x in range(len(data))])
            time.sleep(speed)
            j-=1
        data[j+1] = key
    return data

