weights = list(map(int, input().split()))
max_scores = list(map(int, input().split()))
scores  = list(map(int, input().split()))

if len(weights) == 0:
    equal_weight = 100 / len(scores)
    weights = [equal_weight] * len(scores)

total = 0
for i in range(len(scores)):
    ratio = scores[i] / max_scores[i]       
    weighted = ratio * weights[i]          
    total += weighted

print(f"Final weighted score is { total:.2f}")

