# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
input_features = {
    "st_a":
        parsing_ops.VarLenFeature(dtypes.int64),
    "a":
        parsing_ops.FixedLenFeature((1, 3),
                                    dtypes.int64,
                                    default_value=[0, 42, 0]),
    "b":
        parsing_ops.FixedLenFeature(
            (3, 3),
            dtypes.string,
            default_value=np.random.rand(3, 3).astype(bytes)),
    # Feature "c" is missing a default, this gap will cause failure.
    "c":
        parsing_ops.FixedLenFeature((2,), dtype=dtypes.float32),
}

# Edge case where the key is there but the feature value is empty
original = example(features=features({"c": feature()}))
self._test(
    {
        "example_names": ["in1"],
        "serialized": [original.SerializeToString()],
        "features": input_features,
    },
    expected_err=(
        errors_impl.OpError,
        "Name: in1, Feature: c \\(data type: float\\) is required"))

# Standard case of missing key and value.
self._test(
    {
        "example_names": ["in1", "in2"],
        "serialized": ["", ""],
        "features": input_features,
    },
    expected_err=(
        errors_impl.OpError,
        "Name: in1, Feature: c \\(data type: float\\) is required"))
