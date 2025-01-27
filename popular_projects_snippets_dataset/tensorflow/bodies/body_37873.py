# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parse_single_example_op_test.py
with self.cached_session() as sess:
    if expected_err:
        with self.assertRaisesWithPredicateMatch(expected_err[0],
                                                 expected_err[1]):
            out = parsing_ops.parse_single_example(**kwargs)
            sess.run(flatten_values_tensors_or_sparse(out.values()))
        exit()
    else:
        # Returns dict w/ Tensors and SparseTensors.
        out = parsing_ops.parse_single_example(**kwargs)
        # Check values.
        tf_result = sess.run(flatten_values_tensors_or_sparse(out.values()))
        _compare_output_to_expected(self, out, expected_values, tf_result)

    # Check shapes.
    for k, f in kwargs["features"].items():
        if isinstance(f, parsing_ops.FixedLenFeature) and f.shape is not None:
            self.assertEqual(tuple(out[k].get_shape()),
                             tensor_shape.as_shape(f.shape))
        elif isinstance(f, parsing_ops.VarLenFeature):
            self.assertEqual(
                tuple(out[k].indices.get_shape().as_list()), (None, 1))
            self.assertEqual(tuple(out[k].values.get_shape().as_list()), (None,))
            self.assertEqual(
                tuple(out[k].dense_shape.get_shape().as_list()), (1,))
