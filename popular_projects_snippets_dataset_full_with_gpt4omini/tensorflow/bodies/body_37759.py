# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
# This exercises a different code path for FastParseSequenceExample than
# testSequenceExampleListWithWrongShapeFails (in that test, we can tell that
# the shape is bad based on the total number of values; in this test, we
# can't tell the shape is bad until we look at individual rows.)
original = sequence_example(
    feature_lists=feature_lists({
        "a": feature_list([int64_feature([2]),
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
    expected_err=(errors_impl.OpError, r"Name: in1, Key: a, Index: 0."
                  r"  Number of (int64 )?values != expected."
                  r"  values size: 1 but output shape: \[2\]"))
