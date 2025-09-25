
nums = list(map(int, input().split()))
n = len(nums)


for i in range(n):
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]


if n < 2:
    print(None)
else:
    max1 = nums[-1]       
    second = None
  
    for k in range(n - 2, -1, -1):
        if nums[k] < max1:
            second = nums[k]
            break

    if second is None:
        print(None) 
    else:
        print(second)
