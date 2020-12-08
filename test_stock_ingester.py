import unittest
from unittest import TestCase

import stock_ingester_tradier as si
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def test_get_five_days(self):
        ingester = si.StockIngester()
        results = ingester.get_last_five_days()
        pprint(results)

        self.assertEqual(True, True)


class TestStockIngester(TestCase):
    def test_get_last_days(self):
        self.fail()
