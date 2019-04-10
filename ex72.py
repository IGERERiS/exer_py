# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fucker = 0
vse = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        line = line.replace("X-DSPAM-Confidence:", '')
        line = line.replace("\n", '')
        # print(line)
        # print(fucker)
        fucker = float(line)
        vse = vse + fucker
        count = count + 1

        #print(line)
#print(count)
print("Average spam confidence:", vse/count)
