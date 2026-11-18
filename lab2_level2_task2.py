a = [int(x) for x in input().split()]
b = []
c = []
for x in a:
    c.append(x)
    if len(c) == 3:
        b.append(c)
        c = []
if len(a) == 0 or len(c) != 0:
    print("Incorrect input")
else:
    print(b)
    d = True
    for i in range(len(b) // 2):
        if b[i] != b[len(b) - 1 - i]:
            d = False
    if d:
        print("Yes")
    else:
        print("No")
