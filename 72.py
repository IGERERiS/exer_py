# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

txt = fh.read()
txt = txt.rstrip()
uptxt = txt.upper()
print(uptxt)
