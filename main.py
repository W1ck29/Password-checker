'''Checking Password Security '''
# TODO ADD MORE HANDLING ERRORS
import logging
import string
from time import sleep
from cl_password import Password
from cl_check_security import HaveIbeenPwnd
from functools import cache

alphabet_lowwer = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
logging.basicConfig(level=logging.INFO)
all_passwords = []

try:
    with open('password.txt','r',encoding='utf8') as file:
        for line in file:
            all_passwords.append(line.strip())   
        if len(all_passwords) == 0:
            raise Exception('FILE DOES NOT HAVE ANY PASSWORDS')     
except FileNotFoundError :
    print('This file does not  exist ')
except Exception as error:
    print(error)

class Main:
    '''Main Class'''
    @staticmethod
    def basic_test(basic_test_password):
        '''Static method checking if password has basic security'''
        base = Password(basic_test_password)
        return base.connect_basic()
    
    @staticmethod
    def leak_test(leak_test_password):
        '''Static method which checks if password was leaked'''
        base = HaveIbeenPwnd(leak_test_password)
        return base.leak_check()

if __name__=='__main__':
    print('-------------'*8)
    WHICH_PASSWORD = 1
    for single_password in all_passwords:
        logging.info(f'CHECKING PASSWORD: {WHICH_PASSWORD}\n')
        WHICH_PASSWORD += 1
        sleep(2)
        logging.info('AT THE BEGINNING BASIC TEST\n')
        Main.basic_test(single_password)
        print('---'*20,'\n')
        sleep(2)
        logging.info('NOW TIME FOR LEAK TEST\n')
        sleep(1)
        Main.leak_test(single_password
        print('---'*20,'\n\n\n\n\n')
