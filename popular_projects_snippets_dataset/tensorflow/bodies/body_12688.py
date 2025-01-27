# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_grad_test.py
x = array_ops.placeholder(
    dtype=dtypes.float32, shape=[1, 4, 4, 3], name='input')
f = constant_op.constant([0.5],
                         dtype=dtypes.float32,
                         shape=[2, 2, 3, 2],
                         name='filter')
y = nn_ops.conv2d(x, f, [1, 1, 1, 1], 'SAME')
self.run_test(x, y)
