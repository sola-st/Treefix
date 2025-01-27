# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
output1 = self._gen_outputs(
    lambda: self._build_ds(10, count=-1), 100, verify_exhausted=False)
output2 = self._gen_outputs(
    lambda: self._build_ds(20, count=-1), 100, verify_exhausted=False)
self.assertNotEqual(output1, output2)
self.assertCountEqual(output1, output2)
