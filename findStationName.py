import geopy
from urllib.request import urlopen

link = "https://www.tesla.com/findus/list/chargers/United+States"
f = urlopen(link)

def extract(line):
              line = line[line.find(">")+1:]
              line = line[:line.find("<")]
              return line

nameList = []
addressList = []
areaList = []
for line in f:
              line = line.decode('utf-8')
              if "locality" in line:
                  areaList.append(extract(line))
              if "org url" in line:
                  nameList.append(extract(line))
              if "street-address" in line:
                  addressList.append(extract(line))
answerList = [", ".join([nameList[i],addressList[i],areaList[i]]) for i in range(len(nameList))]
answerList = [elem for elem in answerList if "coming soon" not in elem]
with open("stationNames.txt",'w') as temp:
    for line in answerList:   
        temp.write(line + '\n')

