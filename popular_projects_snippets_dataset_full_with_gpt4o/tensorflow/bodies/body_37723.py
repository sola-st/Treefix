# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
if expected_err:
    if not context.executing_eagerly():
        with self.assertRaisesWithPredicateMatch(expected_err[0],
                                                 expected_err[1]):
            self.evaluate(parsing_ops.parse_example(**kwargs))
    else:
        with self.assertRaises(Exception):
            parsing_ops.parse_example(**kwargs)
    exit()
else:
    out = parsing_ops.parse_example(**kwargs)
    _compare_output_to_expected(self, out, expected_values)

# Check shapes; if serialized is a Tensor we need its size to
# properly check.
serialized = kwargs["serialized"]
batch_size = (
    self.evaluate(serialized).size
    if isinstance(serialized, ops.Tensor) else np.asarray(serialized).size)
for k, f in kwargs["features"].items():
    if isinstance(f, parsing_ops.FixedLenFeature) and f.shape is not None:
        self.assertEqual(tuple(out[k].shape.as_list()), (batch_size,) + f.shape)
    elif isinstance(f, parsing_ops.VarLenFeature):
        if context.executing_eagerly():
            out[k].indices.shape.assert_is_compatible_with([None, 2])
            out[k].values.shape.assert_is_compatible_with([None])
            out[k].dense_shape.shape.assert_is_compatible_with([2])
        else:
            self.assertEqual(out[k].indices.shape.as_list(), [None, 2])
            self.assertEqual(out[k].values.shape.as_list(), [None])
            self.assertEqual(out[k].dense_shape.shape.as_list(), [2])
