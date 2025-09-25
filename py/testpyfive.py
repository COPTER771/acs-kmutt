n = int(input().strip())
a = list(map(int, input().split()))

status = "safe"
for i in range(1, n):
    if a[i] < a[i-1]:
        status = "dangerous"
        break

print(status)