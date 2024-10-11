# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
ctx = context.context()
ctx.ensure_initialized()

a_2_by_2 = random_ops.random_uniform((2, 2))
b_2_by_2 = random_ops.random_uniform((2, 2))

self.assertAllClose(
    math_ops.add_n([a_2_by_2, b_2_by_2]),
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "AddN", None,
                                      [a_2_by_2, b_2_by_2]))
