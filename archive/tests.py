from unittest import TestCase

from archive.models import replace_umlauts


class Test_replace_umlauts(TestCase):
    def test_umlauts_should_be_replaced(self):
        self.assertEqual("ae", replace_umlauts("ä"))
        self.assertEqual("aeoeue", replace_umlauts("äöü"))
        self.assertEqual("ssome Uemlauts", replace_umlauts("ßome Ümlauts"))
