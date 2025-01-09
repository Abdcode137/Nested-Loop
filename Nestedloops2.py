Lower = int(input("Enter The Lower range:"))
Upper = int(input("Enter The Upper range:"))

print("Prime Numbers Between", Lower ,"And", Upper)

for num in range(Lower , Upper + 1):

    if (num > 1):
        for i in range (2 , num):
         if (num % i == 0):
            break
        else:
            print(num) 