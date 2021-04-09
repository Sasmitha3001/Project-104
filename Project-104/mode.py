import csv
from collections import Counter

f=open('Project104Data.csv')
read=csv.reader(f)
data=list(read)
data.pop(0)

newData=[]
for i in range(len(data)):
    num=data[i][2]
    newData.append(float(num))

modeData=Counter(newData)

modeDataRange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}

for weight,occurence in modeData.items():
    if 50<float(weight)<60:
        modeDataRange['70-80']+=occurence
    elif 60<float(weight)<70:
        modeDataRange['70-80']+=occurence
    elif 70<float(weight)<80:
        modeDataRange['70-80']+=occurence

modeRange,modeOccurence=0,0

for i,occurence in modeDataRange.items():
    if occurence>modeOccurence:
        modeRange=[int(i.split('-')[0]),int(i.split('-')[1])]
        modeOccurence=occurence
mode=float((modeRange[0]+modeRange[1])/2)
print("Mode is: "+str(mode))
