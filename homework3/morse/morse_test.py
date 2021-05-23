import pytest
import morse


@pytest.mark.parametrize('i,exp', [
    ('... --- ...', 'SOS'),
    ('.--. .. -. -.-. ....', 'PINCH'),
    ('..- -. .. -', 'UNIT'),
    ('.. .- -- --. .-. --- --- -',
     'IAMGROOT')
])
def test_decode(i, exp):
    assert morse.decode(i) == exp
