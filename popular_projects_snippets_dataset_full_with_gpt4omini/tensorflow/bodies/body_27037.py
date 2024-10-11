# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/shuffle_and_repeat_test.py
output1 = self._gen_outputs(lambda: self._build_ds(10), 100)
output2 = self._gen_outputs(lambda: self._build_ds(10), 100)
self.assertEqual(output1, output2)
