import re
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

for line in handle:
    line = line.rstrip()

    y =  re.findall('X-DSPAM-Confidence: ([0-9.]+)', line)
    y =  re.findall('\S+?@\S+', line)

    # atpos =  line.find('@')
    # spos = line.find(' ', atpos)
    # if spos > -1:
    #     print(line[atpos: spos])

    if y == []:   continue
    print(y)
