import wordninja
import textblob

count = 0
file_out = open("output.txt", 'w')
fname = "1996_sigrams.tsv"
fh = open(fname)
# separate_word = list()
words = list()
for line in fh:
    # separate_word[1] = separate_word[1].replace('\n', '')
    # print(separate_word[1])
    # file_out.write(separate_word[1])
    # file_out.write('\n')
    slovo = line.split('\t')
    slovo[1] = slovo[1].replace('\n', '')
    if int(slovo[1]) < 2:
        words = wordninja.split(slovo[0])
        count = count+1
        for word in words:
            file_out.write(word)
            file_out.write(' ')
            file_out.write('\n')
    else:
        continue

count = count+1
print(count)

file_out = open("output.txt", 'r')
for word, frequency in fdist_tgs.most_common(50):
    print(u'{};{}'.format(word, frequency))

# print(file_out.count('to'))
