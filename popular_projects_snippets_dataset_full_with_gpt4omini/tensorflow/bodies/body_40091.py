# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

@custom_gradient.recompute_grad
def f(x):
    exit(math_ops.reduce_prod(math_ops.tanh(x)**2))

with self.assertRaisesRegex(NotImplementedError,
                            "recompute_grad tried to transpose"):
    primals = [constant_op.constant([1.])]
    sym_jac_fwd = _jacfwd(f, primals)
