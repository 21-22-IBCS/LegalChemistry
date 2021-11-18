def CoffeShop():

    return


def main():
    
    print("Welcome to the CoffeeShop")
    
    name = input("what is your name?")
    print("Hello" + name)
    order = input("How can i take your order?")

    print("Thanks. Here is the receipt: ")
    ordernumber = 0
    
    print("\n\n\n\nreceipt:\nOrder:" + name + "\norder: " + order + "\nordernumber: " + str(ordernumber))



if __name__=="__main__":
    main()


#palindrome
def palindrome(string):
    opposite_str = str(string[::-1])
    if string == opposite_str:
        print("True")
    else:
        print("False")
    
def main():
    coffeeShop()
    word = input("\nEnter word to check palindrome: ")
    palindrome(word)
    
if __name__ == "__main__":
    main()



