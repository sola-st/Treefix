# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default():
    w = constant(1.0, shape=[2, 2])
    x = constant(1.0, shape=[2, 2])
    wx = math_ops.matmul(w, x)
    split_wx = array_ops.split(value=wx, num_or_size_splits=2, axis=0)
    c = math_ops.reduce_sum(split_wx[1])
    gw = gradients.gradients(c, [w])[0]
self.assertEqual("MatMul", gw.op.type)
