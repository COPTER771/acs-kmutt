blockk = 0
num = 1
while num != 0:
    num = int(input())
    if(num > blockk):
        blockk = num
print(f"The highest weight is: {blockk}")