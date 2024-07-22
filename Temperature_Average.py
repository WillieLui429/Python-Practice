import statistics

path = "C:\\Users\\willi\\OneDrive\\Documents\\temperature.txt"
with open(path) as file:
    file = open(path,"rt")
temp = []

for i in file:
    holder = i.split()
    for j in holder:
        if j.isdigit():
            temp.append(int(j))
        else:
            pass


print(temp)
print(statistics.mean(temp))
file.close()