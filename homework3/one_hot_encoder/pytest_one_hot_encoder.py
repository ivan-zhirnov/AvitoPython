import pytest
import one_hot_encoder


def test_ok_for_copies():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_ok_for_sequence_without_copy():
    cities = ['Moscow', 'Liberty']
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Moscow', [0, 1]),
        ('Liberty', [1, 0]),
    ]
    assert actual == expected


def test_ok_repeated_liberty():
    cities = {'Liberty', 'Liberty', 'Liberty'}
    actual = one_hot_encoder.fit_transform(cities)
    expected = [
        ('Liberty', [1]),
    ]
    assert actual == expected


def test_ok_if_will_be_exception():
    with pytest.raises(Exception):
        one_hot_encoder.fit_transform(111)