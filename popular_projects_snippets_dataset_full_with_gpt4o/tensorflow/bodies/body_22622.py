# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl_test.py
if is_sparse:
    var0 = variables.Variable([[0.0], [0.0]], dtype=dtype)
    var1 = variables.Variable([[0.0], [0.0]], dtype=dtype)
    grads0 = indexed_slices.IndexedSlices(
        constant_op.constant([0.1], shape=[1, 1], dtype=dtype),
        constant_op.constant([0]), constant_op.constant([2, 1]))
    grads1 = indexed_slices.IndexedSlices(
        constant_op.constant([0.02], shape=[1, 1], dtype=dtype),
        constant_op.constant([1]), constant_op.constant([2, 1]))
else:
    var0 = variables.Variable([0.0, 0.0], dtype=dtype)
    var1 = variables.Variable([0.0, 0.0], dtype=dtype)
    grads0 = constant_op.constant([0.1, 0.2], dtype=dtype)
    grads1 = constant_op.constant([0.01, 0.02], dtype=dtype)

update = opt.apply_gradients(zip([grads0, grads1], [var0, var1]))
self.evaluate(variables.global_variables_initializer())

sess = ops.get_default_session()
v0_val, v1_val = self.evaluate([var0, var1])
if is_sparse:
    self.assertAllCloseAccordingToType([[0.0], [0.0]], v0_val)
    self.assertAllCloseAccordingToType([[0.0], [0.0]], v1_val)
else:
    self.assertAllCloseAccordingToType([0.0, 0.0], v0_val)
    self.assertAllCloseAccordingToType([0.0, 0.0], v1_val)

# Run Ftrl for a few steps
for _ in range(steps):
    update.run()

v0_val, v1_val = self.evaluate([var0, var1])
exit((v0_val, v1_val))
