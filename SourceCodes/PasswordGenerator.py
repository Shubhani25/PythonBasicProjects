import random

name = input('Please enter your name:')
print('Hey',name,'! Let me help you by generating a random passcode for you.')

chars = 'QWERTYUIOPLKJHGFDSAZXCVBNMqazwsxedcrfvtgbyhnujmikolp-_*&^%$#@!.<>,?/[]{()}\|+='

length = int(input('Enter the length of password required.'))

password = ''
for char in range(length):
    password += random.choice(chars)
print('Suggested Password:', password)

print('Hope this helped!')