x=37
while x>36:
    input_palindrome=input("Please type in the letters: ")
    a=0
    b=-1
    head=(input_palindrome[a])
    back=(input_palindrome[b])
    while head==back:
        a=a+1
        b=b-1
        head=(input_palindrome[a])
        back=(input_palindrome[b])
        if a<=int(len(input_palindrome))-2:
            continue
        elif a>int(len(input_palindrome))-2:
            print("")
            print("palindrome("+input_palindrome+")->True")
            print("")
            break
    else:
        print("")
        print("palindrome("+input_palindrome+")->False")
        print("")
    
