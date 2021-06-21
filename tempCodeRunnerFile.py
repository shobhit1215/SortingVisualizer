def bubble_sort(data):
    for _ in range(len(data-1)):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]


data= [7,3,4,9,10,1]
bubble_sort(data)
print(data)