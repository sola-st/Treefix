# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/parse_example_dataset_test.py
original = [example(features=features({"a": float_feature([1, 1, 3]),})),]

serialized = [m.SerializeToString() for m in original]

self._test(
    ops.convert_to_tensor(serialized),
    {"a": parsing_ops.FixedLenFeature(None, dtypes.float32)},
    expected_err=(ValueError, "Missing shape for feature a"))
