# import collections

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

list_list = []


for line in handle:
    if 'From ' in line:
        tmp_list = line.split()
        two_letters = tmp_list[5].split(':')
        list_list.append(two_letters[0])

dict = {}
count = 0

for item in list_list:
    dict[item] = list_list.count(item)

# tups = dict.items()
# print(sorted(dict.items()))

for key, value in sorted(dict.items()):
    print(key, value)
