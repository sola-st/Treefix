# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
# Asserting the iterator is exhausted after producing 100 items should fail.
with self.assertRaises(AssertionError):
    self._gen_outputs(lambda: self._build_ds(10, count=None), 100)
with self.assertRaises(AssertionError):
    self._gen_outputs(lambda: self._build_ds(10, count=-1), 100)
