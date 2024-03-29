def no_dups(s):
    word_set = set()
    words = s.split()
    for word in words:
        word_set.add(word)
    return " ".join(word_set)

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))