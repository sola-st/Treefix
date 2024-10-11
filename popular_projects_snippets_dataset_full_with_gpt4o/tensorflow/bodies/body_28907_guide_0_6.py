import unittest # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def assertDatasetProduces(self, dataset, expected_output): # pragma: no cover
        iterator = dataset_ops.make_one_shot_iterator(dataset) # pragma: no cover
        next_element = iterator.get_next() # pragma: no cover
        sess = tf.compat.v1.Session() # pragma: no cover
        self.assertEqual(sess.run(next_element), expected_output) # pragma: no cover
mock_test = MockTest() # pragma: no cover
self = mock_test # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
