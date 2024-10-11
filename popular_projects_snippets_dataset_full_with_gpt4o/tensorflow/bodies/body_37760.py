# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = sequence_example(feature_lists=feature_lists({}))

# Test fails because we didn't add:
#  feature_list_dense_defaults = {"a": None}
self._testBoth(
    {
        "example_name": "in1",
        "serialized": ops.convert_to_tensor(original.SerializeToString()),
        "sequence_features": {
            "a": parsing_ops.FixedLenSequenceFeature((2,), dtypes.int64)
        }
    },
    expected_err=(
        errors_impl.OpError,
        "Name: in1, Feature list 'a' is required but could not be found."
        "  Did you mean to include it in"
        " feature_list_dense_missing_assumed_empty or"
        " feature_list_dense_defaults?"))
