def retrieve_words(f):
    
    fulltext = f.read()
    list0Text = fulltext.split(" ")
    return list0Text

def average_word_length(word_list):
    """
    Given a list of words, calculate avg word length
    
    eg. ['hello', 'world', 'foo', 'bar']

    after list comprehension: [5,5,3,3]
    after sum: 16
    return 16 / 4
    """

    return sum([len(word) for word in word_list]) / len(word_list)

def clean_up_word_list(word_list):
    clean_list = []

    
    
    return clean_list
    
def main():


    # string data type
   # word = "apple"
    #empty = ""
   # large = "sdhjfgs djfbgjkdfg hdkjfgnhjd ksfhgjk asjhfbgjasgjdf kberifagjksbjsdfbjgb"
 

    #split example
    #sentence = "i like you."
    #splitSentence = sentence.split(" ")
   # print(splitSentence)

    

    # text files
    f = open("odyssey.txt", "r")
    word_list = retrieve_words(f)

    # TODO: cleanup word list
    # get rid of empty strings
    # take out non alphabets

    # apply avg length, no clean up
    print("word length:{}".format(average_word_length(word_list)))
    
    
    
if __name__== "__main__":
    main()
