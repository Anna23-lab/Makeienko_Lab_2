a = [int(x) for x in input().split()]
a.sort(reverse=True)
s = 0
for i in range(5):
    s = s + a[i] ** 3
print(s)
