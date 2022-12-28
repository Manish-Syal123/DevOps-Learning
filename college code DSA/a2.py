def accept():
    dsa=[]
    n=int(input("Enter the student count of class : "))
    for i in range(n):
        print("Enter the marks scored in dsa for student %i: "%(i+1))
        var=int(input())
        dsa.append(var)
    print("\n1. Marks stored in dsa : ")
    for i in range(n):
        print("Student %i:"%(i+1),dsa[i])
    return dsa
def average(dsa):
    sum=0
    for i in range (len(dsa)):
        if(dsa[i]!=-1):
            sum=sum+dsa[i]
            avg=sum/len(dsa)
    print("2. Average score of class : ", avg)
    print(" SUM = ", sum)
def highlow(dsa):
    print("3. Highest score and the lowest score of class : ")
    large=dsa[0]
    for i in range(len(dsa)):
        if(large<dsa[i]):
            large=dsa[i]
    print("Highest marks of class : ",large)
    for i in range(len(dsa)):
        if(dsa[i]!=-1):
            small=dsa[i]
            break
    for j in range(len(dsa)):
        if(dsa[j]!=-1):
            if(small>dsa[j]):
                small=dsa[j]
    print("Samllest marks of class : ",small)
def absent(dsa):
    count=0
    print("4. Count of students who were absent for the test : ")
    for i in range(len(dsa)):
        if(dsa[i]==-1):
            count=count+1
            print("Absent Student roll number is : %i"%(i+1))
            print("Absent student count is : ",count)
def highfre(dsa):
    max1=0
    for i in range(len(dsa)):
        if(dsa[i]!=-1):
            var=dsa.count(dsa[i])
    if(var>max1):
        max1=var
        res=dsa[i]
        print("5. Mark with highest frequency ",res)
        print("count : ",max1)
while True:
    print("1.Accept")
    print("2.Average score")
    print("3.Highest and lowest score")
    print("4.Absend count")
    print("5.Highest Frequency")
    print("6.Exit\n")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        dsa=accept()
    elif(ch==2):
        average(dsa)
    elif(ch==3):
        highlow(dsa)
    elif(ch==4):
        absent(dsa)
    elif(ch==5):
        highfre(dsa)
    if(ch==6):
        break
