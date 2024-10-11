# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = sequence_example(
    feature_lists=feature_lists(
        {"a": feature_list([float_feature([2, 3])])}))

serialized = original.SerializeToString()

self._testBoth(
    {
        "example_name": "in1",
        "serialized": ops.convert_to_tensor(serialized),
        "sequence_features": {
            "a": parsing_ops.FixedLenSequenceFeature((2,), dtypes.int64)
        }
    },
    expected_err=(errors_impl.OpError,
                  "Feature list: a, Index: 0.  Data types don't match."
                  " Expected type: int64"))
