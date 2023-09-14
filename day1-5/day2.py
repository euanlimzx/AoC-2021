with open("day2.in") as file:
    data = [i for i in file.read().strip().split("\n")]

# print(data)

h, d, aim = 0,0,0

for i in range(len(data)):
    if data[i][0] == "f":
        h += int(data[i][-1])
        d += int(data[i][-1]) * aim
    elif data[i][0] == "d":
        aim += int(data[i][-1])
    elif data[i][0] == "u":
        aim -= int(data[i][-1])

print(h,d, h*d)