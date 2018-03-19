print("Write a word")
word=input()
l = len(word)
i = 2
if  l <= i:
    print(word)
else:
    print(word[0] + word[1] +  word[l-2] + word[l-1])

