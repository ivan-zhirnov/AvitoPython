import unittest
import one_hot_encoder


class TestTF(unittest.TestCase):

    def test_ok_for_copies(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_ok_for_sequence_without_copy(self):
        cities = ['Moscow', 'Liberty']
        actual = one_hot_encoder.fit_transform(cities)
        expected = [
            ('Moscow', [0, 1]),
            ('Liberty', [1, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_ok_if_liberty_in_sequence_is(self):
        cities = ['Moscow', 'liberty']
        actual = one_hot_encoder.fit_transform(cities)
        self.assertIn(('liberty', [1, 0]), actual)

    def test_ok_if_will_be_exception(self):
        with self.assertRaises(Exception):
            one_hot_encoder.fit_transform(111)