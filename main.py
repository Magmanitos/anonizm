s = [int(x) for x in open("17_2024.txt")]
max13 = max(x for x in s if x % 100 == 13)
res = []
for i in range(len(s)-2):
    three = range(100, 1000)
    if ((s[i] in three) + (s[i + 1] in three) + (s[i + 2] in three)) == 2 and \
        sum(s[i:i + 3]) <= max13:
        res.append(sum(s[i:i + 3]))
print(len(res), max(res))
