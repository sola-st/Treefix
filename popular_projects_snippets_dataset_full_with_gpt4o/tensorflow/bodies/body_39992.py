# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
input_tensor, mask = self._boolean_mask_input()

self._run(lambda: self._boolean_mask_fn(input_tensor, mask), 10000)
