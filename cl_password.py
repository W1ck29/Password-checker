'''Basic PASSWORD test'''
import logging
import string
from functools import cache
alphabet_lowwer = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
numbers = [1,2,3,4,5,6,7,8,9,0]

@cache
class Password:
    '''Class Password'''
    def __init__(self,passwords):
        self.passwords = passwords

    def check_len(self):
        """Checking if passwords has more than 7 symbols"""
        if len(self.passwords) >= 8:
            logging.info('Password has 8 or more symbols!')
            return True
        logging.warning('Password has less than 8 symbols')
        return False

    def  check_if_num(self):
        '''Checking if password has a number'''
        check = 0
        for letter in self.passwords:
            try:
                int(letter)
            except ValueError:
                check += 1
        if check != len(self.passwords):
            logging.info('Password has numbers')
            return True
        logging.warning('This password does not contain any numbers')
        return False

    def check_if_special_symbol(self):
        '''Checking if password has a special symbol'''
        characters = ['!', '@', '$', '#', '%', '^', '&', '*', '(', ')',
                '_', '-', '=', '+', '{',
                '[', '}', ']', ':', ';', "'", '"', '\\', '|',
                '>', '.', '<', ',', '?', '/',
                       ]
        for letter in self.passwords:
            if letter in characters:
                logging.info('Password has special symbols')
                return True
        logging.warning('Password does not contain any special symbols')
        return False

    def check_lower_upper(self):
        '''Checking if password has lower and upper case symbols'''
        upper = 0
        lower = 0
        for letter in self.passwords:
            if letter in numbers:
                pass
            elif letter in alphabet_upper:
                upper +=1
            elif letter in alphabet_lowwer:
                lower += 1
        if lower > 0 and upper >0:
            logging.info('Password has lower and upper case symbols')
            return True
        logging.warning('Password  does not have lower or upper case symbols!')
        return False

    def connect_basic(self):
        '''Checking if all requrements are approved'''
        tester = all([
            self.check_if_num(),
            self.check_if_special_symbol(),
            self.check_lower_upper(),
            self.check_len()
                      ])
        if  tester is True:
            logging.info('All requirements are met')
            return True
        logging.warning('Your password need some correct!')
        return False
        