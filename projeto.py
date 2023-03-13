import random

response = input('Você quer jogar dado ? [Y/N] ')
while response == 'y':
    number = random.randint(1,6)
    if (number == 1):
        print('[-----]')
        print('[    ]')
        print('[  0 ]')
        print('[    ]')
        print('[-----]')
    if (number == 2):
        print('[-----]')
        print('[0    ]')
        print('[     ]')
        print('[    0]')
        print('[-----]')
    if (number == 3):
        print('[-----]')
        print('[0    ]')
        print('[  0  ]')
        print('[    0]')
        print('[-----]')
    if (number == 4):
        print('[-----]')
        print('[0   0]')
        print('[     ]')
        print('[0   0]')
        print('[-----]')
    if (number == 5):
        print('[-----]')
        print('[0   0]')
        print('[  0  ]')
        print('[0   0]')
        print('[-----]')
    if (number == 6):
        print('[-----]')
        print('[0 0 0]')
        print('[     ]')
        print('[0 0 0]')
        print('[-----]')
    response = str(input('Você quer jogar dado ? [Y/N] '))

if (response == 'n'):
    print('Então não me pertuba más meu!')