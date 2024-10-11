# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
dict_elements = [{
    "foo": 1,
    "bar": 4.0
}, {
    "foo": 2,
    "bar": 5.0
}, {
    "foo": 3,
    "bar": 6.0
}]
verify_fn(
    self, lambda: self._build_list_dataset(dict_elements), num_outputs=3)
