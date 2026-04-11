data = "once upon a time, there was a beginner programmer who wanted to learn python. he started with basic syntax and gradually moved on to more complex topics. he practiced coding every day and eventually became proficient in python programming."
def longest_word(s):
    words = s.split()
    lenth = 1
    longword = ''
    for word in words:
        if len(word)> lenth:
            lenth= len(word)
            longword= word
    
    return lenth, longword


res = longest_word(data)
print(res)