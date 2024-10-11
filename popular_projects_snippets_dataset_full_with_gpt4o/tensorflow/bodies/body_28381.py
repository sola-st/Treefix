# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
num_outputs = sum((x**2) % 2 == 0 for x in range(10))
verify_fn(self, self._build_filter_dict_dataset, num_outputs)
