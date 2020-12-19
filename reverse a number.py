''' To reverse a given numbers. '''

def rev(a):
    b=""
    str_a = str(a)
    for i in str_a:
        b=i+b
    return int(b)

a = str(input("Enter the number to be reverse :"))
print('The reverse of the given number ',a,'is ',rev(a))
