# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
with ops.Graph().as_default():
    a_2_by_2 = constant_op.constant(1.0, shape=[2, 2])
    m = resource_variable_ops.ResourceVariable(a_2_by_2)
ctx = context.context()
ctx.ensure_initialized()
with self.assertRaises(core._FallbackException):
    pywrap_tfe.TFE_Py_FastPathExecute(ctx, "MatMul", None, m, m,
                                      "transpose_a", False, "transpose_b",
                                      False)
