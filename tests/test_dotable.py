import unittest
import re
from dotable import *

class TestDotable(unittest.TestCase):
    def test_hash_replace(self):
        d1 = Dotable.parse({'a': [{'b': 3, 'c': 5}]})
        d2 = Dotable.parse([42, {'a': 'shrubbery'}])

        s = '#{d1.a[0].b} #{d2[1].a}'

        result = re.sub('#({[^}]*})', r'\1', s).format(**locals())
        expected = '3 shrubbery'
        self.assertEquals(result, expected)