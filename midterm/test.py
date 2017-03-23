f = open('mcdonalds.csv', 'r')
sen = f.readline()
print(sen)
lst = sen.split(',')
for x in lst:
    print(x)
    print()
