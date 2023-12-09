#Challenge 2

import re
file = open("input.txt", "r")
combined = []
words = ["one", "two", "three", "four","five", "six", "seven", "eight", "nine"]
converted = ["1","2","3","4","5","6","7","8","9"]
total = 0
for line in file:
    if words in line:
        index = words.index(words)
        line.replace(converted[index])
    num1 = re.search("\d", line).group(0)
    num2 = re.search(".*(\d)", line).group(1)
    combined.append(int(num1 + num2))
print(sum(combined))

#Answer is 
