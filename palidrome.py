''' To check a given number or word is palidrome or not. '''

def rev(a):
    b=""
    str_a = str(a)
    for i in str_a:
        b=i+b
    return b

a = str(input("Enter the word to check palidrime:"))
b = rev(a)
print(a,b,type(a),type(b))
if a==b:
    print("It is palindrome")
else:
    print("It is not palindrome")
