import csv

f=open('Project104Data.csv')
read=csv.reader(f)
data=list(read)
data.pop(0)

newData=[]
for i in range(len(data)):
    num=data[i][2]
    newData.append(float(num))

length=len(newData)
sum=0
for i in newData:
    sum=sum+i

mean=sum/length
print("Mean is: "+str(mean))

