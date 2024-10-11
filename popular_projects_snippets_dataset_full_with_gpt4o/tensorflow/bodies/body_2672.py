# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
a_vals = np.array(
    [[2, 0, 0, 0], [3, 6, 0, 0], [4, 7, 9, 0], [5, 8, 10, 11]],
    dtype=np.float32)
b_vals = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                  dtype=np.float32)

c = self._NewComputation()
ops.TriangularSolve(
    ops.Constant(c, a_vals),
    ops.Constant(c, b_vals),
    left_side=False,
    lower=True,
    transpose_a=ops.TriangularSolveOptions_Transpose.TRANSPOSE,
    unit_diagonal=False)
self._ExecuteAndCompareClose(
    c,
    expected=[
        np.array([
            [0.5, 0.08333334, 0.04629629, 0.03367003],
            [2.5, -0.25, -0.1388889, -0.1010101],
            [4.5, -0.58333331, -0.32407406, -0.23569024],
        ],
                 dtype=np.float32)
    ],
    rtol=1e-4)
