dic = {}
for i in range(2,11):
    dic[str(i)] = i
dic['Jack'] = 11
dic['Queen'] = 12
dic['King'] = 13
dic['Ace'] = 14
c1 = dic[input()]
c2 = dic[input()]
c3 = dic[input()]
c4 = dic[input()]
c5 = dic[input()]
c6 = dic[input()]

print(sum([c1, c2, c3, c4, c5, c6]) / 6)
