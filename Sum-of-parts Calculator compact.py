output = 0
lowest = int(input("Please define a range you want (lowest number):"))
highest = int(input("Please define a range you want (highest number):"))
for i in range(lowest,highest + 1): output += i
print(output)
input("Press enter to exit.")