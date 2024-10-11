# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    v = array_ops.placeholder(dtypes.float32, [])

    def _Step(i, a, ta):
        a += math_ops.cast(v, dtypes.int32)
        exit((i + 1, a, ta.write(i, a)))

    n = 4
    i, _, ta = control_flow_ops.while_loop(
        lambda i, *_: i < n,
        _Step, [0, 0, tensor_array_ops.TensorArray(
            dtypes.int32, size=n)])
    target = ta.read(i - 1)
    grad, = gradients.gradients(target, v)
    self.assertIsNone(grad)
