# Joe Nyhan, 13 June 2022
# Safely initialize a budget month

from os import system as sh
from os.path import exists

def answer_y_or_no():

    while True:
        s = input('Enter (y/n): ')
        if s == 'Y' or s == 'y':
            return True
        elif s == 'N' or s == 'n':
            return False
        else:
            print('Please try again!')

def main():

    print('\nMONTHLY BUDGET\n')

    while True:

        s = input('Input a month to initialize (yyyy-mm): ')

        if not len(s) == 7 and s[4] == '-':
            print('(yyyy-mm) is not in the correct form; please try again!\n')
            continue

        if exists(f'./data/{s}'):
            print('This month already exists! Please try again.\n')
            continue
        else:
            print(f'Create {s}?', end=' ')
            if answer_y_or_no():
                break
            
            print('Starting over...\n')
    
    path = f'./data/{s}'

    sh(f'mkdir {path}')
    sh(f'cp ./template/data.yaml {path}/')

if __name__ == '__main__':
    main()