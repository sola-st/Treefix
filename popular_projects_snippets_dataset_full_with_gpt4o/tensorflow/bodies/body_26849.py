# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
div = 3
num_outputs = sum(x % 3 != 2 for x in range(100))
verify_fn(self, lambda: self._build_filter_range_graph(div), num_outputs)
