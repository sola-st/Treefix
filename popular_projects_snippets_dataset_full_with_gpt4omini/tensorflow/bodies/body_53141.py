# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/graph_util_test.py
with ops.Graph().as_default() as g:
    const_0 = constant_op.constant(5.0)
    with g.device("/device:GPU:0"):
        const_1 = constant_op.constant(5.0)
    with g.device("/device:GPU:1"):
        const_2 = constant_op.constant(5.0)
    with g.device("/device:CPU:0"):
        const_3 = constant_op.constant(5.0)
    with g.device("/device:CPU:1"):
        const_4 = constant_op.constant(5.0)
    with g.device("/job:ps"):
        const_5 = constant_op.constant(5.0)

self.assertDeviceEqual(const_0.device, None)
self.assertDeviceEqual(const_1.device, "/device:GPU:0")
self.assertDeviceEqual(const_2.device, "/device:GPU:1")
self.assertDeviceEqual(const_3.device, "/device:CPU:0")
self.assertDeviceEqual(const_4.device, "/device:CPU:1")
self.assertDeviceEqual(const_5.device, "/job:ps")
