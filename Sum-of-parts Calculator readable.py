#A SIMPLE SUM-OF-PARTS CALCULATOR

#resetting output
output = 0
#asking for a range
lowest = int(input("Please define a range you want (lowest number):"))
highest = int(input("Please define a range you want (highest number):"))
#making sure the funtion stops once it reaches the range
for i in range(lowest,highest + 1):
    #adding one to the output, so it keeps going
    output += i
#printing the output
print(output)
input("Press enter to exit.")