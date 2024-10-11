# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/importer_test.py
with self.cached_session():
    # The default message byte limit is 64M. Ours is 2G with a warning at 512.
    # Adding a 130M entries float32 tensor should exceed the warning, but not
    # the hard limit.
    input_shape = [130, 1000, 1000]
    tensor_input = np.ones(input_shape, dtype=np.float32)
    t = constant_op.constant(tensor_input, shape=input_shape)
    g = array_ops.identity(t)
    self.evaluate(g)
