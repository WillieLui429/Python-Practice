from Employee_Class import Employee
def ranked(firstlist,num):
    holder = 0
    count = 0
    counter = 0
    for i in range(0, len(firstlist)):
        if firstlist[i].rank == 0:
            if float(firstlist[i].Sales) > float(holder):
                holder = firstlist[i].Sales
                count = counter
        else:
            pass
        counter += 1
    firstlist[count].rank = num
    return count
def file_opener(path):
    with open(path) as file:
        file = open(path, "rt")
    firstname = []
    lastname = []
    Street = []
    City = []
    State = []
    Zip_Code = []
    Emp_ID = []
    Location = []
    Salary = []
    Phone_Number = []
    Sales = []
    for i in file:
        holder = i.split()
        count = 1
        for j in holder:
            if count == 1:
                firstname.append(j)
            elif count == 2:
                lastname.append(j)
            elif count == 3:
                Street.append(j)
            elif count == 4:
                City.append(j)
            elif count == 5:
                State.append(j)
            elif count == 6:
                Zip_Code.append(j)
            elif count == 7:
                Emp_ID.append(j)
            elif count == 8:
                Location.append(j)
            elif count == 9:
                Salary.append(j)
            elif count == 10:
                Phone_Number.append(j)
            elif count == 11:
                Sales.append(j)
            count += 1

    file.close()
    mylist = []
    for x in range(0,3):
        mylist.append(Employee(firstname[x], lastname[x], Street[x], City[x], State[x], Zip_Code[x],Emp_ID[x], Location[x], Salary[x],Phone_Number[x],Sales[x]))

    return mylist







path ="C:\\Users\\willi\\OneDrive\\Documents\\work.txt"
newlist = file_opener(path)
first = ranked(newlist,1)
newlist[first].rank = 1
second = ranked(newlist,2)
newlist[second].rank =2
third =ranked(newlist,3)
newlist[third].rank = 3
print("{:^15}{:^20}{:^20}{:^15}{:^15}{:^15}{:^10}".format("Name","Location","Phone Number","Salary","Sales","Total","Rank"))
for i in range(len(newlist)):
    print("{:^15}{:^20}{:^20}{:^15}{:^15}{:^15}{:^10}".format(newlist[i].first_name + " " + newlist[i].last_name,newlist[i].Location,newlist[i].Phone_Number,newlist[i].Salary,newlist[i].Sales,float(newlist[i].Salary) + float(newlist[i].Sales),newlist[i].rank))


