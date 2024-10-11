# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
original = sequence_example(
    feature_lists=feature_lists({
        "a":
            feature_list([int64_feature([2, 3]),
                          int64_feature([2, 3, 4])]),
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
    expected_err=(
        errors_impl.OpError,
        # message from ParseSingleExample.
        r"Name: in1, Key: a, Index: 1."
        r"  Number of int64 values != expected."
        r"  values size: 3 but output shape: \[2\]"
        # or message from FastParseSequenceExample
        r"|Feature list 'a' has an unexpected number of values.  "
        r"Total values size: 5 is not consistent with output "
        r"shape: \[\?,2\]"))
