# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
xs = [1, 2, 3]
self._run(lambda: ops.convert_to_tensor(xs), 1000)
