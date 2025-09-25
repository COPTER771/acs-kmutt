
def multiplication_table(start, end):
    for row in range(1, start + 1):
        for col in range(1, end + 1):
            print(f"{row * col:4}", end="")
        print()
        
print("multiplication_table(5, 9)")
multiplication_table(5, 9)

print()
print("multiplication_table(10, 15)")
multiplication_table(10, 15)
