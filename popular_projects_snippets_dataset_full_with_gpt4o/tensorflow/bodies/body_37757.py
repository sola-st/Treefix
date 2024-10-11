# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = sequence_example(
    feature_lists=feature_lists({
        "a":
            feature_list([
                int64_feature([3, 4]),
                int64_feature([1, 2]),
                float_feature([2.0, 3.0])
            ])
    }))

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
                  "Name: in1, Feature list: a, Index: 2."
                  "  Data types don't match. Expected type: int64"))
