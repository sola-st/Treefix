import unittest # pragma: no cover

class TFRecordWriterTest(unittest.TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        self._num_records = 8 # pragma: no cover
        self.assertEqual(self._num_records, 8) # pragma: no cover

import unittest # pragma: no cover

class TFRecordWriterTest(unittest.TestCase): # pragma: no cover
    def setUp(self): # pragma: no cover
        super(TFRecordWriterTest, self).setUp() # pragma: no cover
        self._num_records = 8 # pragma: no cover
if __name__ == '__main__': # pragma: no cover
    unittest.main() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/tf_record_writer_test.py
from l3.Runtime import _l_
super(TFRecordWriterTest, self).setUp()
_l_(9902)
self._num_records = 8
_l_(9903)
