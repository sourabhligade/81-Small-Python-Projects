"""This program hacks messages encrypted with the Caesar 
cipher by doing a brute force attack agaist every possible key."""

print('Ceaser Cipher by Sourabh Ligade')
f
# Let the user specify the message to hack:
print('Enter the encrypted Caesar cipher message to hack.')
messege=input('>')
f
# Every possible symbol that can be encrypted/decrypted:
# (This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated=''
#decrypt each symbol in the messege
for symbol in messege:
    if symbol in SYMBOLS:
        num=SYMBOLS.find(symbol)
        num-=key

    #handle if number is less than zero:
        if num<0:
            num+=len(SYMBOLS)

        # Add decrypted number's symbol to translated:
            translated+=SYMBOLS[num]
    else:
        # Just add the symbol without decrypting:
        translated+=symbol    

 # Display the key being tested, along with its decrypted text:
print('Key #{}: {}'.format(key,translated))
