n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

for j in data:
    if j % 2 == 1:
        print("T")
    else:
        print("F")