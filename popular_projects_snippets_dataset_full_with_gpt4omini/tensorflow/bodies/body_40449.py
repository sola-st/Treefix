# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py
with ops.Graph().as_default(), self.cached_session():
    t = constant_op.constant(1, dtype=dtypes.float32, shape=(10, 4))
    x = constant_op.constant(2, dtype=dtypes.float32, shape=(10, 4))
    with backprop.GradientTape() as tape:
        tape.watch(x)
        x1, _ = array_ops.split(x, num_or_size_splits=2, axis=1)
        y1 = x1**2
        y = array_ops.concat([y1, t], axis=1)
    exit(self.evaluate(tape.gradient(y, x)))
