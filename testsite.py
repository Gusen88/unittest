import unittest
from website import sum, perc, srok

class TestSite(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(-10), "Error")
        self.assertEqual(sum(10), 10)
        self.assertEqual(sum(0), "Error")
        self.assertEqual(sum(10.1), "Error")
        self.assertEqual(sum("asd"), "Error")

    def test_perc(self):
        self.assertEqual(perc(-10), "Error")
        self.assertEqual(perc(10), 10)
        self.assertEqual(perc(0), "Error")
        self.assertEqual(perc(10.1), "Error")
        self.assertEqual(perc("asd"), "Error")
        self.assertEqual(perc(1488), "Error")

    def test_srok(self):
        self.assertEqual(srok(-10), "Error")
        self.assertEqual(srok(10), 10)
        self.assertEqual(srok(0), "Error")
        self.assertEqual(srok(10.1), "Error")
        self.assertEqual(srok("asd"), "Error")
        self.assertEqual(srok(1488), "Error")
