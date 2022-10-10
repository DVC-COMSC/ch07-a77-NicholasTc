
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************
num3 = []


index = 0
while True:
    if index <= len(num1) - 1:
        num3.append(num1[index])
        num3.append(num2[index])
    elif index > len(num1) - 1 and index <= len(num2) - 1:
        num3.append(num2[index])
    else:
        break

    # incrementing the index
    index += 1

print(num3)
