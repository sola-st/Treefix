# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec_test.py
for bad_name in ["foo", "", "hello world"]:
    with self.assertRaises(ValueError):
        type_spec.register(bad_name)
