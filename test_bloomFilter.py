from random import randint
from unittest import TestCase

from BloomFilter import BloomFilter


class TestBloomFilter(TestCase):
    def setUp(self):
        self.b_filter = BloomFilter()
        self.control = set()
        for i in range(0, 400):
            elem = randint(0, 1000)
            self.b_filter.add_element(elem)
            self.control.add(elem)

    def test_check_element(self):
        for i in range(0, 100000):
            elem = randint(0, 1000)
            if not self.b_filter.check_element(elem):
                self.assertTrue(elem not in self.control)
