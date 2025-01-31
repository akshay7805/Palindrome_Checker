def palindrome_checker(value,length):
    for i in range(0,length):
        if value[i]!=value[length-i-1]:
            return False
        return True
    
    


value=input("Enter the value: ")
str(value)
length=len(value)
print(length)


if palindrome_checker(value,length)==True:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")        