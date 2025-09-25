def strength(passwords):
    results = []
    for pwd in passwords:
        # ตรวจสอบความยาวก่อน
        if len(pwd) < 8:
            results.append("weak")
            continue

        # ตรวจสอบว่ามีตัวอักษรแต่ละประเภทหรือไม่
        has_lower = any(c.islower() for c in pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(not c.isalnum() for c in pwd)

        if len(pwd) >= 12 and has_lower and has_upper and has_digit and has_special:
            results.append("strong")
        else:
            results.append("ok")
    return results


# ---- Test cases ----
print(strength(["abc", "school2025", "LearnIngAI2025!"]))
# Expected: ['weak', 'ok', 'strong']

print(strength(["12345", "abcdefg"]))
# Expected: ['weak', 'weak']

print(strength(["Abc12", "Password!", "Hello2025"]))
# Expected: ['weak', 'ok', 'ok']

print(strength(["MyPass123", "GoodOne2023!", "UltraStrongP@ssw0rd2025!!"]))
# Expected: ['ok', 'strong', 'strong']
