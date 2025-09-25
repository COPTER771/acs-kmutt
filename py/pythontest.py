seconds = int(input().strip())

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"{hours} ชั่วโมง {minutes} นาที {secs} วินาที")
