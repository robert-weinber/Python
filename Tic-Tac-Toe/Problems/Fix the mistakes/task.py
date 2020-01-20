text = input()
words = text.split()
for word in words:
    word_parts = word.split('.')
    if (word.lower().startswith('https://') or word.lower().startswith('http://') or word.lower().startswith('www')) and len(word_parts)>1 or len(word.lower().replace('localhost',''))!=len(word):
        print(word)
    # finish the code here
