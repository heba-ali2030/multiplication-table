# multiplication table
number= int(input("choose a number: "))
count= 1
while count <= 12:
    result= number* count
    print(number, "X", count, "=", result)
    count= count + 1

print('This is the reverse of multiplication table')

# reverse-multipication table
count= 12
while count >= 1:
    result= number* count
    print(number, "X", count, "=", result)
    count= count - 1