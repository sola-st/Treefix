# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/test_utils.py
if op_kwargs is None:
    op_kwargs = kwargs

# compute with op.
with backprop.GradientTape() as gt:
    for var_ in vars_:
        gt.watch(var_)
    y = compute_op(**op_kwargs)  # uses op and decomposites by the graph pass.
    grads = gt.gradient(y, vars_)  # uses registered gradient function.

# compute with composition
with backprop.GradientTape() as gt:
    for var_ in vars_:
        gt.watch(var_)
    re_y = compute_composite(**kwargs)  # uses composite function.
    re_grads = gt.gradient(re_y, vars_)  # uses gradients compposite function.

for v, re_v in zip(y, re_y):
    self.assertAllClose(v, re_v)
for g, re_g in zip(grads, re_grads):
    self.assertAllClose(g, re_g)
