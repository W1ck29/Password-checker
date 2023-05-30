'''Sending password to HaveIbeenPWnd'''
import logging
from hashlib import sha1
from requests import get

class LeakedError(Exception):
    pass

class HaveIbeenPwnd:
    '''Class which test if password was in some database leak'''
    def __init__(self,haslo:str):
        self.haslo = haslo
        self._to_bytes = bytes(self.haslo,encoding='utf8')
        self._hashing = sha1(self._to_bytes)
        self._hashing = self._hashing.hexdigest()
    def _connect(self):
        '''Connecting to api'''       
        send_to_page = 'https://api.pwnedpasswords.com/range/' + self._hashing[:5]
        response = get(send_to_page,timeout=10)
        counter = response.text.splitlines()
        return counter
    def leak_check(self):
        '''Checking if password was leaked'''
        page_response = self._connect()
        for hashed_password in page_response:
            splited_hash = hashed_password.split(':')[0]
            try:
                if splited_hash == self._hashing[5:].upper():
                    raise LeakedError()
            except LeakedError as error:
                logging.critical('YOUR PASSWORD WAS LEAKED')
                return error
        logging.info('Your password was not leaked you can sleep calm <3')
        return True
    