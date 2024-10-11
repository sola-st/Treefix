# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/from_list_test.py
with self.assertRaises(ValueError):
    from_list.from_list(elements._obj)
