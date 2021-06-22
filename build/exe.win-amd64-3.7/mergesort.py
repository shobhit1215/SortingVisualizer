import time

def mergesort(data,drawData,speed):
    merge_sort_alg(data,0,len(data)-1,drawData,speed)


def merge_sort_alg(data,left,right,drawData,speed):
    if left<right:
        mid = (left+right) //2
        merge_sort_alg(data,left,mid,drawData,speed)
        merge_sort_alg(data,mid+1,right,drawData,speed)
        merge(data,left,mid,right,drawData,speed)

def merge(data,left,middle,right,drawData,speed):
    drawData(data,getColorArray(len(data),left,middle,right))
    time.sleep(speed)
    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]
    leftIdx=rightIdx = 0
    for dataIdx in range(left,right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx +=1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx+=1
    drawData(data,['green' if x>=left and x<=right else 'white' for x in range(len(data))])
    time.sleep(speed)

def getColorArray(length , left , middle , right):
    colorArray = []
    for i in range(length):
        if i>=left and i<=right:
            if i>=left and i<=middle:
                colorArray.append('yellow')
            else:
                colorArray.append('pink')
        else:
            colorArray.append('white')
    return colorArray


        