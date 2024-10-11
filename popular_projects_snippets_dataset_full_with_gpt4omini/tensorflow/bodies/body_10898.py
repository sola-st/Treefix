# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default() as g:
    w = constant(1.0, shape=[1, 1])
    x = constant(1.0, shape=[1, 2])
    with g.device("/device:GPU:0"):
        wx = math_ops.matmul(w, x)
    gw = gradients.gradients(wx, [w], colocate_gradients_with_ops=True)[0]
self.assertEqual(gw.op.colocation_groups(), wx.op.colocation_groups())
