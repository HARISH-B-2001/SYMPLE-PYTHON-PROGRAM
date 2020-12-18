def get_sqrt(num):
    sqroot = num
    while abs(num - sqroot * sqroot) > precision:
        print(sqroot)
        sqroot = (sqroot + num/sqroot) / 2
    return sqroot
num = float(input("Enter the number:"))
precision = float(input("Enter the precision value:"))
print(get_sqrt(num))
