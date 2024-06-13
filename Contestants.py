path = "C:\\Users\\willi\\OneDrive\\Documents\\Contestants.txt"

with open(path) as file:

    holder = open(path,"r")
item = []
worker = []
price = []
for x in holder:
    holder2 = x.split()
    for i in holder2:
        if i.isnumeric():
            item.append(i)
        elif i.isalpha():
            worker.append(i)
        else:
            price.append(i)
print(item)
print(worker)
print(price)
saving = []
totalsaving = 0
averagesaving = 0
totalitem = 0
for j in range(0,len(item)):
    totalitem += int(item[j])
    saving.append(float(item[j])*float(price[j]))
    totalsaving += saving[j]

print(saving)
print(totalitem)

print("{:^15}{:^8}{:^10}{:^15}".format("Contestant","Items","AMT","Total Saved"))
for i in range(0,len(item)):
    print("{:^15}{:^8}{:^10}{:^15}".format(worker[i],item[i],price[i],float(item[i])*float(saving[i]),))
print("Total items bought with savings: " + str(totalitem))
print("Average saved is " + str(round((totalsaving/3),2)))
file.close()
