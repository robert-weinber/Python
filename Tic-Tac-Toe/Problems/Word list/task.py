text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
hossz = int(input())
my_list = list()
for sent in text:
        for word in sent:
                if len(word) <= hossz:
                        my_list.append(word)
print(my_list)
