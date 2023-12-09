#Challenge 2

import re
file = open("input.txt", "r")
combined = []
for line in file:
    if "one" in line:
        line = line.replace("one", "1")
    if "two" in line:
        line = line.replace("two", "2")
    if "three" in line:
        line = line.replace("three", "3")
    if "four" in line:
        line = line.replace("four", "4")
    if "five" in line:
        line = line.replace("five", "5")
    if "six" in line:
        line = line.replace("six", "6")
    if "seven" in line:
        line = line.replace("seven", "7")
    if "eight" in line:
        line = line.replace("eight", "8")
    if "nine" in line:
        line = line.replace("nine", "9")
    print(line, end="")
    num1 = re.search("(\d).*", line).group(1)
    num2 = re.search(".*(\d)", line).group(1)
    combined.append(int(num1 + num2))
print(combined)
print(sum(combined))

#Answer is 
