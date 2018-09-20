import unittest
import logging,sys
from searcher.anagram import get_anagrams

class TestAnagrams(unittest.TestCase):
    '''
    A file check test can be written here with input file name being the parameter
    while instantiating the Anagrams class.

    '''
    def setUp(self):
        self.logging = logging.getLogger( "Anagrams.testGetAnagrams" )

    def log_test(self,*args):
        self.logging.debug("Running test: %s, inputs = %s",self._testMethodName,*args)

    def test_anagrams(self):
        inputs = ['plates','eat']
        self.log_test(inputs)
        self.assertEqual(get_anagrams(inputs[0]), ['palest', 'pastel', 'petals', 'plates', 'staple'])
        self.assertEqual(get_anagrams(inputs[1]), ['ate', 'eat', 'tea'])


if __name__ == "__main__":
    TestAnagrams().test_anagrams()