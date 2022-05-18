from datetime import datetime
import main


def test_parse_datetime():
    actual = main.parse_datetime('18.05.2022', '22:08')
    expected = datetime(year=2022, month=5, day=18, hour=22, minute=8)
    assert actual == expected
    

def test_is_now_past():
    test_data = main.parse_datetime('18.05.2022', '22:08')
    now = datetime(year=2022, month=5, day=18, hour=22, minute=9, second=30)
    assert main.is_now(now, test_data) == 'past'
    
    
def test_is_now_past2():
    test_data = main.parse_datetime('18.05.2022', '22:08')
    now = datetime(year=2022, month=5, day=18, hour=22, minute=8, second=30)
    assert main.is_now(now, test_data) == 'past'
    

def test_is_now_now():
    test_data = main.parse_datetime('18.05.2022', '22:08')
    now = datetime(year=2022, month=5, day=18, hour=22, minute=8, second=20)
    assert main.is_now(now, test_data) == 'now'
    
def test_is_now_now2():
    test_data = main.parse_datetime('18.05.2022', '22:08')
    now = datetime(year=2022, month=5, day=18, hour=22, minute=7, second=40)
    assert main.is_now(now, test_data) == 'now'
    
def test_is_now_now3():
    test_data = main.parse_datetime('18.05.2022', '22:08')
    now = datetime(year=2022, month=5, day=18, hour=22, minute=7, second=30)
    assert main.is_now(now, test_data) == 'now'
    
def test_is_now_future():
    test_data = main.parse_datetime('18.05.2022', '22:08')
    now = datetime(year=2022, month=5, day=18, hour=22, minute=6, second=40)
    assert main.is_now(now, test_data) == 'future'

 


