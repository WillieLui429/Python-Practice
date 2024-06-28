def order(firstlist):
    secondlist=[eval(i) for i in firstlist]
    orderedlist = []
    while len(secondlist) > 0:
        count = secondlist[0]
        for j in secondlist:
            if count > j:
                count = j
        orderedlist.append(count)
        secondlist.remove(count)
    return orderedlist


def file_opener(path):
    with open(path) as file:
        holder = open(path, "rt")

    mylist = []
    for i in range(0, 5):
        mylist.append(holder.readline())

    list1 = []

    for j in mylist:
        holder2 = j.rstrip('\n').split(',')
        for x in holder2:
            list1.append(x)
    list2 = []
    for i in list1:
        list2.append(i.split())
    file.close()
    return list2


path = "C:\\Users\\willi\\OneDrive\\Documents\\numbers.txt"
newlist = file_opener(path)
newerlist = []
for i in newlist:
    holder = i
    for j in holder:
        newerlist.append(j)

print(newerlist)
orlist = order(newerlist)
print(orlist)