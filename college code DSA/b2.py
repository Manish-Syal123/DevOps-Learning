def accept_per(A):
    no = int(input("Enter the total number of students : "))
    for i in range(no):
        A.append(float(input("Enter percentage of Student {0} : ".format(i+1))))
    print("Array accepted successfully")
# Printing the percentage of the Students
def print_per(A):
    no=len(A)
    if(no==0):
        print("No data found")
    else:
        print("FE marks :", end=' ')
        for i in range(no):
            print("%f "%A[i],end = ' ')
            print("\n")

def selection_sort(A): #in ascending order
    no=len(A)
    for i in range (no-1): # position = 0 to 6
        min=i
        for j in range (i+1,no): # 0 to position =1 
            if(A[j]<A[min]):
                min=j
        temp=A[i]
        A[i]=A[min]
        A[min]=temp

def bubble_sort(A): 
    no=len(A)
    for i in range(0,no-1): 
        for j in range(no-i-1): 
            if(A[j]>A[j+1]): 
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp 
def main():
    A=[]
    while True:
        print("\n\n1.Accept and display marks")
        print("2.selection sort")
        print("3.bubble sort and top five scores")
        print("4.exit")
        ch = int(input("Enter your choice (from 1 to 4) : "))
        if ch == 4:
            print("End of Program")
            break
        elif ch == 1:
            accept_per(A)
            print_per(A)
        elif ch == 2:
            print("Marks before performing selection Sort : \n")
            print_per(A)
            selection_sort(A)
            print("Marks after performing selection Sort : \n")
            print_per(A)
        elif ch == 3:
            print("Marks before performing bubble Sort : \n")
            print_per(A)
            bubble_sort(A)
            print("Marks after performing bubble Sort : \n")
            print_per(A)
            if(len(A)>=5):
                print("Top five percentage")
                for i in range (5):
                    print("\t %f", A[i])
            else:
                print("Top Scorers")
                for i in range (len(A)):
                    print("\t %f"%A[i])
        else:
            print("wrong choice entered!! Try again") 
main()
