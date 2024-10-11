# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
edit_distance = array_ops.edit_distance(
    hypothesis=hypothesis_st, truth=truth_st, normalize=normalize)

if expected_err_re is None:
    self.assertEqual(edit_distance.get_shape(), expected_shape)
    output = self.evaluate(edit_distance)
    self.assertAllClose(output, expected_output)
else:
    with self.assertRaisesOpError(expected_err_re):
        self.evaluate(edit_distance)
