# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
expected_context_values = expected_context_values or {}
expected_feat_list_values = expected_feat_list_values or {}
expected_length_values = expected_length_values or {}

if expected_err:
    with self.assertRaisesWithPredicateMatch(expected_err[0],
                                             expected_err[1]):
        if batch:
            self.evaluate(parsing_ops.parse_sequence_example(**kwargs))
        else:
            self.evaluate(parsing_ops.parse_single_sequence_example(**kwargs))
else:
    if batch:
        (context_out, feat_list_out,
         lengths_out) = parsing_ops.parse_sequence_example(**kwargs)
    else:
        (context_out,
         feat_list_out) = parsing_ops.parse_single_sequence_example(**kwargs)
        lengths_out = {}

    # Check values.
    _compare_output_to_expected(self, context_out, expected_context_values)
    _compare_output_to_expected(self, feat_list_out,
                                expected_feat_list_values)
    _compare_output_to_expected(self, lengths_out, expected_length_values)

# Check shapes; if serialized is a Tensor we need its size to
# properly check.
if "context_features" in kwargs:
    for k, f in kwargs["context_features"].items():
        if isinstance(f, parsing_ops.FixedLenFeature) and f.shape is not None:
            if batch:
                self.assertEqual(tuple(context_out[k].shape.as_list()[1:]), f.shape)
            else:
                self.assertEqual(tuple(context_out[k].shape.as_list()), f.shape)
        elif isinstance(f, parsing_ops.VarLenFeature) and batch:
            if context.executing_eagerly():
                context_out[k].indices.shape.assert_is_compatible_with([None, 2])
                context_out[k].values.shape.assert_is_compatible_with([None])
                context_out[k].dense_shape.shape.assert_is_compatible_with([2])
            else:
                self.assertEqual(context_out[k].indices.shape.as_list(), [None, 2])
                self.assertEqual(context_out[k].values.shape.as_list(), [None])
                self.assertEqual(context_out[k].dense_shape.shape.as_list(), [2])
        elif isinstance(f, parsing_ops.VarLenFeature) and not batch:
            if context.executing_eagerly():
                context_out[k].indices.shape.assert_is_compatible_with([None, 1])
                context_out[k].values.shape.assert_is_compatible_with([None])
                context_out[k].dense_shape.shape.assert_is_compatible_with([1])
            else:
                self.assertEqual(context_out[k].indices.shape.as_list(), [None, 1])
                self.assertEqual(context_out[k].values.shape.as_list(), [None])
                self.assertEqual(context_out[k].dense_shape.shape.as_list(), [1])
