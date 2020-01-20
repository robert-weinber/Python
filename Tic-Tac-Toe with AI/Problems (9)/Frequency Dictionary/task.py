words = input().lower().split(' ')
word_counter = {}
for word in words:
    word_counter[word] = word_counter.get(word, 0) + 1
for key, value in word_counter.items():
    print(str(key) + ' ' + str(value))
