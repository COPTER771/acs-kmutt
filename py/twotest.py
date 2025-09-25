N = int(input())


data = list(map(int, input().split()))

if N % 2 == 1:
    median = data[N // 2]
else:
    mid1 = data[N // 2 - 1]
    mid2 = data[N // 2]
    median = (mid1 + mid2) / 2

print("{:.2f}".format(median))
