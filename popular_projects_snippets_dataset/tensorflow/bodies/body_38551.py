# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
np_expected_values = np.array(expected_values)
np_expected_indices = np.array(expected_indices)
with self.cached_session():
    values_op, indices_op = nn_ops.top_k(inputs, k, sorted=sorted)
    values, indices = self.evaluate([values_op, indices_op])

    self.assertShapeEqual(np_expected_values, values_op)
    self.assertShapeEqual(np_expected_indices, indices_op)

    if sorted:
        self.assertAllClose(np_expected_values, values)
        # Do some special casing of equality of indices: if indices
        # are not the same, but values are floating type, ensure that
        # the values are within epsilon of each other.
        if not np.issubdtype(np_expected_values.dtype, np.floating) and \
            np_expected_values.dtype != dtypes.bfloat16.as_numpy_dtype:
            # Values are not floating point type; check indices exactly
            self.assertAllEqual(np_expected_indices, indices)
        else:
            # Values are floating point; indices may be swapped for
            # values near each other.
            indices_not_equal = np_expected_indices != indices
            if np.any(indices_not_equal):
                values_unsure = values[indices_not_equal]
                expected_values_unsure = expected_values[indices_not_equal]
                self.assertAllClose(expected_values_unsure, values_unsure)
    else:
        np_inputs = np.array(inputs)

        # Check that the indices are valid.
        for result_index, src_index in np.ndenumerate(indices):
            value = values[result_index]
            expected_value = np_inputs[result_index[0], src_index]
            np.testing.assert_almost_equal(value, expected_value)

        # Check that if two elements are equal, the lower-index element appears
        # first.
        shape = values.shape
        for batch_index in range(shape[0]):
            for index in range(shape[1] - 1):
                if np.isclose(values[batch_index, index],
                              values[batch_index, index + 1]):
                    self.assertLess(indices[batch_index, index],
                                    indices[batch_index, index + 1])

        # Now check the results, ignoring order.
        self.assertAllEqual(np.sort(np_expected_indices), np.sort(indices))
        self.assertAllClose(np.sort(np_expected_values), np.sort(values))
