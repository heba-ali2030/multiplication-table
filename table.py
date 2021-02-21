# multiplication table
method= input('choose N for normal table and R for reverse table:  ')
number= int(input("choose a number: "))
if method =='N':
    count= 1
    while count <= 12:
        result= number* count
        print(number, "X", count, "=", result)
        count= count + 1

# reverse-multipication table
elif method == 'R':
    count= 12
    while count >= 1:
         result= number* count
         print(number, "X", count, "=", result)
         count= count - 1

else:
    print('please choose N or R to complete: ')