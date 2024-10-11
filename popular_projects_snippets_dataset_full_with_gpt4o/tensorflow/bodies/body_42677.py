# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
ctx = context.context()
ctx.ensure_initialized()

a_2_by_2 = constant_op.constant(1.0, shape=[2, 2])
m = resource_variable_ops.ResourceVariable(a_2_by_2)
x = pywrap_tfe.TFE_Py_FastPathExecute(ctx, "MatMul", None, m,
                                      m, "transpose_a", False,
                                      "transpose_b", False)
y = pywrap_tfe.TFE_Py_FastPathExecute(ctx, "MatMul", None,
                                      a_2_by_2, a_2_by_2, "transpose_a",
                                      False, "transpose_b", False)

self.assertAllEqual(x, y)
