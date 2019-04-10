#Binary Converter - from anythink to binary
#Denary to binary conversion
st = input("Input what do you want to convert in binary:")
# while denary>0:
print("Your phrase translated to binary will be:")
for letter in st:
  #A left shift in binary means /2
  print(format(ord(letter), 'b'), end = ' ')

print()
#Binary to denary conversion
# text = input("Input what do you want to convert from binary:")
# text.decode('utf-8')
# # string  = text.decode('utf-8')
# print("Your string is: ", string)
