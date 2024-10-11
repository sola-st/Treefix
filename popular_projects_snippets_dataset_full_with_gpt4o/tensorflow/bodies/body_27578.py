# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
original = [
    example(features=features({
        "a": float_feature([1]),
    })), example(features=features({}))
]

serialized = [m.SerializeToString() for m in original]

expected_output = {
    "a":
        np.array(
            [[1], [-1]], dtype=np.float32)  # 2x1 (column vector)
}

self._test(
    ops.convert_to_tensor(serialized), {
        "a":
            parsing_ops.FixedLenFeature(
                (1,), dtype=dtypes.float32, default_value=-1),
    },
    expected_values=expected_output,
    create_iterator_twice=True)
