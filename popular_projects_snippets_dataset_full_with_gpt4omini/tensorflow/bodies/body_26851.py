# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
num_outputs = sum((x**2) % 2 == 0 for x in range(10))
# pylint: disable=unnecessary-lambda
verify_fn(self, lambda: self._build_filter_dict_graph(), num_outputs)
