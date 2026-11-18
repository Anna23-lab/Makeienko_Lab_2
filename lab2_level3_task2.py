a = int(input())
b = {i for i in range(1, 101)}
for i in range(a):
    c = input()
    if c == "HELP":
        print(*sorted(b))
        break
    d = set(map(int, c.split(", ")))
    e = input()
    if e == "Yes":
        b = b & d
    else:
        b = b - d
