def reverse(number):
    rev=0
    while(number>0):
        rem=number % 10
        rev=rev*10+rem
        number =number//10
        print(rev)
    return rev
def checkpalindrome(number):
    x=reverse(number)
    print(f"reversed of numbrr {x}")
    print(f"oryyfujb{number}")
    if x ==number:
        print("palindrome")
    else:
        print("not plndmr")
checkpalindrome(123)