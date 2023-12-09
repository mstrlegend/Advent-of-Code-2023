#Challenge 1

import re
file = open("input.txt", "r")
combined = []
total = 0
for line in file:
    num1 = re.search("\d", line).group(0)
    num2 = re.search(".*(\d)", line).group(1)
    combined.append(int(num1 + num2))
print(sum(combined))

#Answer is correct, confirmed to be 55816
