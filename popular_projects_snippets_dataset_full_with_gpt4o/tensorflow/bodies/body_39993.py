# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
input_tensor, mask = self._boolean_mask_input()
compiled_fn = def_function.function(self._boolean_mask_fn)

self._run(lambda: compiled_fn(input_tensor, mask), 10000)
