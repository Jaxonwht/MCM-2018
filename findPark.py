tempList = []
with open("parking_garage_list.csv",'r') as f:
    for line in f:
        line = line.split(",")
        tempList.append(line[4]+" "+line[6]+" "+line[7]+" "+line[11])

with open("stationNames.txt",'w') as f:
    k = 0
    for entry in tempList:
        k += 1
        if k == 1:
            continue
        if entry.startswith("\""):
            entry = entry[1:]
        f.write(entry+"\n")

