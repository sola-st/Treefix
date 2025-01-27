# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/noop_elimination_test.py
name, transformation, expected = case
exit(result + combinations.combine(
    init_dataset_fn=make_range,
    transformation=combinations.NamedObject(name, transformation),
    expected_name=expected))
