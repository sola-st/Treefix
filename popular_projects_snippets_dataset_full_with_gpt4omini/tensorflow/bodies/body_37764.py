# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
"""FeatureList with 2 value tensors but only one splits tensor."""
original = sequence_example(
    feature_lists=feature_lists({
        "b_values":
            feature_list(
                [float_feature([1, 2, 3, 4]),
                 float_feature([2, 4, 6])]),
        "b_splits":
            feature_list([int64_feature([0, 1, 4])]),
    }))
sequence_features = {
    "b":
        parsing_ops.RaggedFeature(
            value_key="b_values",
            dtype=dtypes.float32,
            partitions=[parsing_ops.RaggedFeature.RowSplits("b_splits")],
            validate=True)
}
self._testBoth(
    dict(
        serialized=ops.convert_to_tensor(original.SerializeToString()),
        sequence_features=sequence_features),
    expected_err=(
        (errors_impl.InvalidArgumentError, ValueError),
        # Message for batch=true:
        "Feature b: values and partitions are not aligned"
        # Message for batch=false in graph mode:
        "|.* do not form a valid RaggedTensor"
        # Message for batch=false in eager mode:
        "|Incompatible shapes|required broadcastable shapes"))
