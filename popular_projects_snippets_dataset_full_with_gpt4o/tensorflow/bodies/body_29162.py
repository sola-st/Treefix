# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/optional_test.py
name, value_fn, expected_structure = y
exit(x + combinations.combine(
    tf_value_fn=combinations.NamedObject(name, value_fn),
    expected_value_structure=expected_structure))
