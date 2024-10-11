# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
if expected_err:
    with self.assertRaisesWithPredicateMatch(expected_err[0],
                                             expected_err[1]):
        self.evaluate(parsing_ops.parse_single_example(**kwargs))
else:
    out = parsing_ops.parse_single_example(**kwargs)
    _compare_output_to_expected(self, out, expected_values)

# Check shapes.
for k, f in kwargs["features"].items():
    if isinstance(f, parsing_ops.FixedLenFeature) and f.shape is not None:
        self.assertEqual(
            tuple(out[k].get_shape()), tensor_shape.as_shape(f.shape))
    elif isinstance(f, parsing_ops.VarLenFeature):
        if context.executing_eagerly():
            self.assertEqual(tuple(out[k].indices.shape.as_list()), (2, 1))
            self.assertEqual(tuple(out[k].values.shape.as_list()), (2,))
            self.assertEqual(tuple(out[k].dense_shape.shape.as_list()), (1,))
        else:
            self.assertEqual(tuple(out[k].indices.shape.as_list()), (None, 1))
            self.assertEqual(tuple(out[k].values.shape.as_list()), (None,))
            self.assertEqual(tuple(out[k].dense_shape.shape.as_list()), (1,))
