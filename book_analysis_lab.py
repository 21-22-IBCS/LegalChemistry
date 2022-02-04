def main():
    f = open("odyssey.txt", "r")

    fulltext = f.read()
    
    listOfText = fulltext.split(" ")

    print(len(listOfText))
    o=0
    p=0

    while not(listOfText[o] == "odyssey.txt") and not(listOfText[o+1] == "*** START OF THE PROJECT GUTENBERG EBOOK THE ODYSSEY ***"):
        o = o + 1

    while not(listOfText[p] == "***") and not(listOfText[p+1] == "*** END OF THE PROJECT GUTENBERG EBOOK THE ODYSSEY ***"):
        p = p + 1


    newList = []
    newnewList = []
    punctuations = '''!@#$%^&*()__+=-/?<>,.~`'''

    for i in range(o+2, p):
        temp = listOfText[i].strip("\n")
        for mm in temp:
            if mm in punctuations:
                temp = temp.replace(mm,"")
        newList.append(temp)

    a = 0
    b = 0
    for j in range(len(newList)):
        if(len(newList[j])>0):
            q = q + 1
            w = w + len(newList[j])
            newnewList.append(newList[j])
    print("avg length of word: " + str(round(s/c,3)))

    q2 = 0
    for k in range(len(newnewList)):
        if newnewList[k] == "and" or newnewList[k] == "but" or newnewList[k] == "or":
            q2 = q2 + 1

    print("Percentage of text in main coordinating conjunctions is: " + str(round(100*q2/len(newnewList), 3)) + "%")

if __name__ == "__main__":
    main()