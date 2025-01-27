# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/pywrap_tfe_test.py
ctx = context.context()
ctx.ensure_initialized()

a_2_by_2 = random_ops.random_uniform((2, 2))
b_2_by_2 = random_ops.random_uniform((2, 2))

with backprop.GradientTape(persistent=True) as tape:
    tape.watch(a_2_by_2)
    tape.watch(b_2_by_2)
    z1 = pywrap_tfe.TFE_Py_FastPathExecute(ctx, "IdentityN",
                                           None, [a_2_by_2, b_2_by_2])
    z2 = array_ops.identity_n([a_2_by_2, b_2_by_2])
dz1_dy = tape.gradient(z1[0], [a_2_by_2])[0]
dz2_dy = tape.gradient(z2[0], [a_2_by_2])[0]
self.assertAllEqual(dz1_dy.numpy(), dz2_dy.numpy())
