# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
with ops.device("/job:dev_v0"):
    v0 = variables.Variable(10.0, name="v0")
with ops.device("/job:dev_v1"):
    v1 = gen_state_ops.variable(
        shape=[1],
        dtype=dtypes.float32,
        name="v1",
        container="",
        shared_name="")
    v1.set_shape([1])
tensor2 = v0 + v1
ema = moving_averages.ExponentialMovingAverage(0.25, name="foo_avg")
with ops.device("/job:default"):
    ema.apply([v0, v1, tensor2])
self.assertDeviceEqual("/job:dev_v0", ema.average(v0).device)
self.assertDeviceEqual("/job:dev_v1", ema.average(v1).device)
# However, the colocation property is maintained.
self.assertEqual([b"loc:@v1"], ema.average(v1).op.colocation_groups())
self.assertDeviceEqual("/job:default", ema.average(tensor2).device)
