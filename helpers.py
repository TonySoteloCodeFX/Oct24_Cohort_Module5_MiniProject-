import os

def clr():
    '''This clears the terminal'''
    os.system('cls' if os.name == 'nt' else 'clear')

def hr(num):
    '''Prints a line with length of given number.'''
    print(f"{'_' * num}\n")