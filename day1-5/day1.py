with open("day1.in") as file:
    data = [i for i in file.read().strip().split("\n")]

# print(data)

res = 0
for i in range(len(data)-3):
    if int(data[i+3]) > int(data[i]):
        res += 1

print(res)