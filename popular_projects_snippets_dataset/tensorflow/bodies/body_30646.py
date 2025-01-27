# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/init_ops_test.py
init = init_ops.identity_initializer()
shape = (10, 5)
with self.session(graph=ops.Graph(), use_gpu=True):
    self.assertAllClose(init(shape), np.eye(*shape))
