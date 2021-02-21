# multiplication table
number= int(input("choose a number: "))
count= 1
while count <= 12:
    product= number* count
    print(number, "X", count, "=", product)
    count= count + 1


# reverse-multipication table
count= 12
while count >= 1:
    product= number* count
    print(number, "X", count, "=", product)
    count= count - 1