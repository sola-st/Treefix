# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
ctx = context.context()
ctx.ensure_initialized()

with backprop.GradientTape(persistent=True) as tape:
    a_2_by_2 = constant_op.constant(1.0, shape=[2, 2])
    tape.watch(a_2_by_2)
    z = pywrap_tfe.TFE_Py_FastPathExecute(ctx, "MatMul", None,
                                          a_2_by_2, a_2_by_2, "transpose_a",
                                          False, "transpose_b", False)
dz_dy = tape.gradient(z, [a_2_by_2])[0]
self.assertAllEqual(dz_dy.numpy(),
                    constant_op.constant(4.0, shape=[2, 2]).numpy())
