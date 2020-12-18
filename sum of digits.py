def add(a):
    b=0
    str_a=str(a)
    for i in str_a:
        b=b+int(i)
    return b
a= int(input("Enter the number:"))
b = add(a)
print("The sum of the digits of given number ",a,"is ",b)
