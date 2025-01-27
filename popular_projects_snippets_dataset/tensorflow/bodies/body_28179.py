# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cardinality_test.py
name, dataset_fn, expected_result = y
exit(x + combinations.combine(
    dataset_fn=combinations.NamedObject(name, dataset_fn),
    expected_result=expected_result))
