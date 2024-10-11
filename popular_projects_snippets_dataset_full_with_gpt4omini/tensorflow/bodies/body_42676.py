# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
a_2_by_2 = random_ops.random_uniform((2, 2))
b_2_by_2 = random_ops.random_uniform((2, 2))

a_100_by_784 = random_ops.random_uniform((100, 784))
b_100_by_784 = random_ops.random_uniform((100, 784))

ctx = context.context()
ctx.ensure_initialized()

self.assertAllClose(
    math_ops.matmul(a_2_by_2, b_2_by_2),
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "MatMul", None,
                                      a_2_by_2, b_2_by_2, "transpose_a",
                                      False, "transpose_b", False))
self.assertAllClose(
    math_ops.matmul(a_100_by_784, b_100_by_784, transpose_b=True),
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "MatMul", None,
                                      a_100_by_784, b_100_by_784,
                                      "transpose_a", False, "transpose_b",
                                      True))
