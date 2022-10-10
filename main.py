
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# ******************************
# Make your Code
# ******************************
num3 = []


index = 0
longer_arr = []
shorter_arr = []
if len(num1) > len(num2):
    longer_arr = num1
    shorter_arr = num2
else:
    longer_arr = num2
    shorter_arr = num1

while True:
    if index <= len(shorter_arr) - 1:
        num3.append(shorter_arr[index])
        num3.append(longer_arr[index])
    elif index > len(shorter_arr) - 1 and index <= len(longer_arr) - 1:
        num3.append(longer_arr[index])
    else:
        break

    # incrementing the index
    index += 1

print(num3)
