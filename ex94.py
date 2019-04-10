name = input("Enter file:")
# if len(name) < 1 :
name = "mbox-short.txt"
handle = open(name)
count = 0
kniga = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        word = words[1]
        kniga[word] = kniga.get(word,0) +1
        count = count+1

bigcount = None
bigemail = None

for email,count in kniga.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigemail = email

print(bigemail, bigcount)


# print("There were", count, "lines in the file with From as the first word")
# print(kniga)
