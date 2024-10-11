# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
"""Verifies that matrix_diag_part produces `solution` when fed `params`.

    Args:
      params: dictionary containing input parameters to matrix_diag_part.
      solution: numpy array representing the expected output.
      high_level: call high_level matrix_set_diag
      rtol: relative tolerance for equality test.
      atol: absolute tolerance for equality test.
    """
input = params["input"]  # pylint: disable=redefined-builtin
with self.session() as session:
    for dtype in self.numeric_types - {np.int8, np.uint8}:
        expected = solution.astype(dtype)
        with self.test_scope():
            params["input"] = array_ops.placeholder(
                dtype, input.shape, name="input")
            if high_level:
                # wraps gen_array_ops.matrix_diag_part_v3
                output = array_ops.matrix_diag_part(**params)
            else:
                # TODO(b/201086188): Remove this case once MatrixDiag V1 is removed.
                output = gen_array_ops.matrix_diag_part(**params)
            output = array_ops.matrix_diag_part(**params)
        result = session.run(output, {
            params["input"]: input.astype(dtype),
        })
        self.assertEqual(output.dtype, expected.dtype)
        self.assertAllCloseAccordingToType(
            expected, result, rtol=rtol, atol=atol, bfloat16_rtol=0.03)
