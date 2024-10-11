# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
with ops.Graph().as_default() as g:
    with g.device("/device:GPU:1"):
        w = constant(1.0, shape=[1, 1])
    x = constant(1.0, shape=[1, 2])
    y = constant(1.0, shape=[1, 2])
    wx = math_ops.matmul(w, x)
    wy = math_ops.matmul(w, y)
    with g.device("/device:GPU:0"):
        z = wx + wy

    gw1 = gradients.gradients(z, [w], colocate_gradients_with_ops=True)[0]
    self.assertEqual(gw1.op.colocation_groups(), wx.op.colocation_groups())

    gw2 = gradients.gradients(z, [w], colocate_gradients_with_ops=False)[0]
    self.assertNotEqual(wx.op.colocation_groups(), gw2.op.colocation_groups())
