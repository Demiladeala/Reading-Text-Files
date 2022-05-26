# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    test = open(filename,"r")
    return test.read()

def count_words():
    text = read_file_content("./story.txt")
    words = list(text.split())
    count = {}
    for i in words:
        if i not in count:
            count[i] = 1
        else:
            count[i] +=1
    return (count)
       
    
print(count_words())
