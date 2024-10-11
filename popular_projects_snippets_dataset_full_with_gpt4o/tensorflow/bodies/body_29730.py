# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batch_gather_op_test.py
params = np.array([[b"asdf", b"zxcv"], [b"qwer", b"uiop"]])
with self.cached_session():
    indices_tf = constant_op.constant([1])
    self.assertAllEqual(
        [[b"qwer", b"uiop"]],
        self.evaluate(array_ops.batch_gather(params, indices_tf)))
