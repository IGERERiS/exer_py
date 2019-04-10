# This program aims to get list of all organizations

file_au=open('1982authors.txt', encoding="utf8", 'r')
file_txt=open('1982.txt', encoding="utf8", 'r')

for line in file_au:
    word_list = line.split()
    print(word_list[-1])
