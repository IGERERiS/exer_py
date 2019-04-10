import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_182444.txt"
handle = open(name)
summa = 0
total = 0

for line in handle:
    line = line.rstrip()

    y =  re.findall('([0-9]+)', line)
    if y == []: continue
    summa = [float(i) for i in y]
    summa = sum(summa)
    total = total + summa

print(int(total))
    # summa = summa +
    # y =  re.findall('\S+?@\S+', line)

    # atpos =  line.find('@')
    # spos = line.find(' ', atpos)
    # if spos > -1:
    #     print(line[atpos: spos])

    # if y == []:   continue
    # print(y)
