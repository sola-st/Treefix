# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_conditional_accumulator_test.py
expected_tensor = _indexedslice(expected_array)
self._assertEqual_indexedslices(expected_tensor, result)
