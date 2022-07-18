import re
fhand = open("regex_sum_1563474.txt")
sum = 0
for line in fhand:
    findnum = re.findall('[0-9]+',line)
    if findnum:
        for num in findnum:
            num = int(num)
            sum+=num
    print(findnum)
print(sum)
