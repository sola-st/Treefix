import unittest # pragma: no cover

self = unittest.TestCase() # pragma: no cover
self.assertRaisesRegex = unittest.TestCase().assertRaisesRegex # pragma: no cover

import unittest # pragma: no cover

class TestMock(unittest.TestCase): # pragma: no cover
    def runTest(self): # pragma: no cover
        pass # pragma: no cover
 # pragma: no cover
self = TestMock() # pragma: no cover
self.assertRaisesRegex = unittest.TestCase().assertRaisesRegex # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
from l3.Runtime import _l_
with self.assertRaisesRegex(TypeError, 'shape dimensions must be integer'):
    _l_(21501)

    fc.numeric_column(
        'aaa', shape=[
            1.0,
        ])
    _l_(21500)

with self.assertRaisesRegex(ValueError,
                            'shape dimensions must be greater than 0'):
    _l_(21503)

    fc.numeric_column(
        'aaa', shape=[
            0,
        ])
    _l_(21502)
