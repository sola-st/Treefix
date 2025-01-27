# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_tensor_slices_test.py
dict_components = {"foo": [1, 2, 3], "bar": [[4.0], [5.0], [6.0]]}

verify_fn(
    self,
    lambda: self._build_tensor_slices_dataset(dict_components),
    num_outputs=3)
