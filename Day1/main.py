with open('day1Input.txt', 'r') as f:
    strings = f.readlines()

totalSum = 0
digitMap = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

for s in strings:
    firstDigit = None
    lastDigit = None

    for i in range(len(s)):
        c = s[i]

        if c.isnumeric():
            if not firstDigit:
                firstDigit = c
            lastDigit = c

        for offset in [3, 4, 5]:
            if i + offset < len(s):
                candidate = s[i:i + offset]
                if candidate in digitMap and not firstDigit:
                    firstDigit = digitMap[s[i:i+offset]]
                elif candidate in digitMap and firstDigit:
                    lastDigit = digitMap[s[i:i+offset]]

    if not lastDigit:
        lastDigit = firstDigit

    totalSum += int(firstDigit + lastDigit)

print(totalSum)