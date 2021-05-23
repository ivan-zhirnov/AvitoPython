  
```python -m doctest -o NORMALIZE_WHITESPACE -v morse.py```
```python
Trying:
    decode('... --- ...')
Expecting:
    'SOS'
ok
Trying:
    decode(".--. .. -. -.-. ....") # doctest: +ELLIPSIS
Expecting:
    'PINCH'
ok
Trying:
    decode('------')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: '------'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode("PINCH") # doctest: +ELLIPSIS
Expecting:
    '.--. ... ....'
ok
Trying:
    encode('z')
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: 'z'
ok
1 items had no tests:
    morse
2 items passed all tests:
   3 tests in morse.decode
   3 tests in morse.encode
6 tests in 3 items.
6 passed and 0 failed.
Test passed.
```
```python
pytest morse_test.py
```
```python
========================================================================================================================= test session starts ==========================================================================================================================
platform win32 -- Python 3.9.1, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: D:\mai\AvitoPython\homework3\morse
collected 4 items                                                                                                                                                                                                                                                       

morse_test.py ....                                                                                                                                                                                                                                                [100%]

========================================================================================================================== 4 passed in 0.05s ===========================================================================================================================
```