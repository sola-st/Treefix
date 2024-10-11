# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/matrix_diag_ops_test.py
"""Verifies that matrix_diag produces `solution` when fed `params`.

    Args:
      params: dictionary containing input parameters to matrix_diag.
      solution: numpy array representing the expected output of matrix_diag.
      high_level: call high_level matrix_diag
      rtol: relative tolerance for equality test.
      atol: absolute tolerance for equality test.
    """
diagonal = params["diagonal"]
with self.session() as session:
    for dtype in self.numeric_types - {np.int8, np.uint8}:
        expected = solution.astype(dtype)
        with self.test_scope():
            params["diagonal"] = array_ops.placeholder(
                dtype, diagonal.shape, name="diagonal")
            if high_level:
                # wraps gen_array_ops.matrix_diag_v3
                output = array_ops.matrix_diag(**params)
            else:
                # TODO(b/201086188): Remove this case once MatrixDiag V1 is removed.
                output = gen_array_ops.matrix_diag(**params)
        result = session.run(output,
                             {params["diagonal"]: diagonal.astype(dtype)})
        self.assertEqual(output.dtype, expected.dtype)
        self.assertAllCloseAccordingToType(
            expected, result, rtol=rtol, atol=atol, bfloat16_rtol=0.03)
