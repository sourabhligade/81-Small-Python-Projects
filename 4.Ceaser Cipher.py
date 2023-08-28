try:
    import pyperclip
except ImportError:
    pass  # If pyperclip is not installed, do nothing.

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('The Caesar cipher encrypts letters by shifting them over by a')


print('key number. For example, a key of 2 means the letter A is')
print('encrypted into C, the letter B encrypted into D, and so on.')
print()

# Let the user enter if they are encrypting or decrypting:
while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('>').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Enter e or d')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Enter the key (0 to {}) to use:'.format(maxKey))
    response = input('>')
    if not response.isdecimal():
        continue

    if 0 <= int(response) <= maxKey:
        key = int(response)
        break

print('Enter the message to {}.'.format(mode))
message = input('>')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = (num + key) % len(SYMBOLS)
        elif mode == 'decrypt':
            num = (num - key) % len(SYMBOLS)

        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass
