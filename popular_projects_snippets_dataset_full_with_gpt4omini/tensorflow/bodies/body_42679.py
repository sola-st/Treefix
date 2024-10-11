# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
ctx = context.context()
ctx.ensure_initialized()

with backprop.GradientTape(persistent=True) as tape:
    a_2_by_2 = constant_op.constant(1.0, shape=[2, 2])
    m = resource_variable_ops.ResourceVariable(a_2_by_2)
    tape.watch(m)
    z = pywrap_tfe.TFE_Py_FastPathExecute(ctx, "MatMul", None, m,
                                          m, "transpose_a", False,
                                          "transpose_b", False)
dz_dy = tape.gradient(z, [m])[0]
self.assertAllEqual(dz_dy.numpy(),
                    constant_op.constant(4.0, shape=[2, 2]).numpy())
