import unittest # pragma: no cover

class CustomTestCase(unittest.TestCase): # pragma: no cover
    def assertDatasetProduces(self, dataset, expected_output): # pragma: no cover
        iterator = dataset.make_one_shot_iterator() # pragma: no cover
        next_element = iterator.get_next() # pragma: no cover
        with tf.Session() as sess: # pragma: no cover
            output = [] # pragma: no cover
            try: # pragma: no cover
                while True: # pragma: no cover
                    output.append(sess.run(next_element)) # pragma: no cover
            except tf.errors.OutOfRangeError: # pragma: no cover
                pass # pragma: no cover
            self.assertEqual(output, expected_output) # pragma: no cover
test_case_obj = CustomTestCase() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/as_numpy_iterator_test.py
from l3.Runtime import _l_
ds = dataset_ops.Dataset.from_tensors((2, None))
_l_(21082)
self.assertDatasetProduces(ds, [(2, None)])
_l_(21083)
