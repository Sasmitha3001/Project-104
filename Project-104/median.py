import csv

f=open('Project104Data.csv')
read=csv.reader(f)
data=list(read)
data.pop(0)

newData=[]
for i in range(len(data)):
    x=data[i][2]
    newData.append(float(x))

newData.sort()
length=len(newData)

if(length%2!=0):
    median=float(newData[length//2])
    print("The Median is: "+str(median))

else:
    num1=float(newData[length//2])
    num2=float(newData[length//2-1])
    median=(num1+num2)//2
    print("The Median is: "+str(median))