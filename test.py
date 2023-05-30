import pytest
from cl_password import Password
from cl_check_security import HaveIbeenPwnd,LeakedError
from requests import get


def test_len_true():

    passw = Password('Kutas123')

    length = passw.check_len()

    assert length == True

def test_len_false():


    passw = Password('Kutas12')

    length = passw.check_len()

    assert length == False

def test_number():
    passw = Password('janek123')

    checker = passw.check_if_num()

    assert checker == True

def test_special_symbol():
    passw = Password('Janek!@#')

    symb = passw.check_if_special_symbol()

    assert symb == True

def test_lower_upper():
    passw = Password('jJanekDzbanek1#')

    checker = passw.check_lower_upper()

    assert checker == True

def test_connect():


    passw = Password('Super!123')

    checker = passw.connect_basic()

    assert checker == True

def test_requests_status_code():
    connection = get('https://api.pwnedpasswords.com/range/A94A8')
    assert connection.status_code == 200

def test_if_leaked_negative():
    conn = HaveIbeenPwnd('qwerty123')

    try:
        conn.leak_check()
    except LeakedError as error:
        assert conn.leak_check() == error

def test_if_leaked_positive():
    conn = HaveIbeenPwnd('!@#amazPasswNo')
    try:
        conn.leak_check()
        assert conn.leak_check() == True
    except LeakedError as error:
        assert conn.leak_check() == error

# ! No idea for more tests 