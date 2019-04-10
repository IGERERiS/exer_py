$ awk '/Get PDF  Export citation\r/{p=0};p;/^SEG\r/{flag=1}' 1982organizations.txt
https://www.coursera.org/learn/python-network-data/lecture/bwvyb/12-4-retrieving-web-pages

# x = input('Vvedite chislo: ')
# x = float(x)
# if x > 50:
#   print('x bolshe 50')
# if x < 50:
#   print('x menshe 50')
# if x == 50:
#   print('x ravno 50')
#
# if x > 50:
#   print('x bolshe 50')
# elif x > 100:
#   print('x bolshe 100')
# else :
#   print('x malenko')
#
#
#
# if x > 100:
#     print('eto slishkom mnogo')
# else:
#     print('Nu ladno, poehali: ')
#     for i in range(1, int(x)):
#         print(i)
#     print("Finish")
#
# astr = "hello Timoha"
# try:
#     istr = int(astr)
# except:
#     istr = - 1
#
# print("First", istr)
#
#
# rastr = input('Vvedite celoe chislo: ')
# try :
#     ival = int(rastr)
# except :
#     ival = -100500
#
# if ival > 0 :
#     print("Krasava")
# else :
#     print("Ty che, ohuel?!")
# hrs = input("Enter Hours: ")
# h = float(hrs)
# rt = 10.50
#
# if h > 40 :
#     Pay = 40*rt + (h % 40)*1.5*rt
# print(Pay)

# score = input("Enter Score: ")
# score = float(score)
#
# if score < 1 :
#     if score > 0 :
#         if score >= 0.9 :
#             print("A")
#
#         elif score >= 0.8 :
#             print("B")
#
#         elif score >= 0.7 :
#             print("C")
#
#         elif score >= 0.6 :
#             print("D")
#
#         elif score < 0.6 :
#             print("F")
#
#
#     else :
#         print("Score is out of range 0-1")
#         quit()
#
# else :
#     print("Score is out of range 0-1")
#     quit()

# def mthfck():
#     print("Knock knock")
#     print("Who is there?")
#     print("Fuck you!")
#
# print("Call the function")
# #
# # mthfck()
#
# def greet():
#     return "Hello"
# print(greet(), "Timoha")
#
# def summ(a, b):
#     prpr = a + b
#     return prpr
#
# print(summ(3545, 5454))

#
# def computepay(h,r):
#     if h > 40 :
#         Pay = 40*rt + (h % 40)*1.5*rt
#     return Pay
#
# hrs = input("Enter Hours:")
# rt = input("Enter Rate:")
# hrs = float(hrs)
# rt = float(rt)
# p = computepay(hrs, rt)
# print(p)

# for i in list(range(10)) :
#     print(i)
# print('Blastoff!')

# friends = ['Olya', 'Sveta', 'Kristina', 'Nastya']
# for friend in friends :
#      print('Ti samaya krasivaya, dorogaya', friend)
# # print('Blastoff!')
#
# import random
# my_array = []
# largest = -100500
# count = 0
# print('Before', largest)
# for ii in list(range(100)):
#     # try:
#     #     x[ii] = random.randint(1,101)
#     my_array.append(random.randint(1,1000))
#     if my_array[ii] > largest:
#         largest = my_array[ii]
#         count = ii
#
# print(my_array)
# print('After', largest, ', number of iteration,', count)


# largest = -100500
# print('Before', largest)
# for the_num in []


# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#
#     if num == "done" :
#         break
#
#     try:
#         fval = float(num)
#     except:
#         print('Invalid input')
#         continue
#
#     if largest is None:
#         largest = fval
#     if smallest is None:
#         smallest = fval
#
#     if largest < fval :
#         largest = fval
#     if smallest > fval:
#         smallest = fval
#
#     # print(num)
#
# print("Maximum is", int(largest))
# print("Minimum is", int(smallest))

# city = 'Antananarivu'
# count = 0
# for letter in city:
#     print(letter)
#     if letter == 'a':
#         count = count +1
# print('Total a letters,', count)

# index = 0
# while index < len (city):
#     letter = city[index]
#     print(index, letter)
#     index = index + 1

#
# word = input('Enter word: ')
# # print(word)
# if word == 'motherfucker':
#     print('Stop cursing, you debil')
#
# if word < 'banana':
#     print('Your word, ' + word + ', comes before banana.')
# elif word > 'banana':
#     print('Your word, ' + word + ', comes after banana.')
# else:
#     print('Spasibo, do svidanja')
# Getting authors from the files
wc -l *authors.txt > lines_amount.txt

awk 'c&&!--c; /full access/{c=2}' _^[1982-2018].txt > testfile.tmp && mv testfile.tmp new.txt
 awk 'c&&!--c; /full access/{c=2}' _*.txt > new.txt
 sed -i 's/\,/\n/g' new.txt

for name in {1982..2018}
do
    sed -i "/pp\./d" $name"authors.txt"
end
done


    awk 'c&&!--c; /full access/{c=2}' _$name".txt" > $name"authors.txt"
done




text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
str = text[pos:pos+6]
num = float(str)
print(num)
