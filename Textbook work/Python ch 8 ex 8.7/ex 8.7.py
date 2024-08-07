#Write a script that displays a table of the character codes in the range of 0 to 255 and the corresponding character

print ('Number: ', 'Character: ')
for a in range (256):
    char = chr(a)
    print (char," | ", a)