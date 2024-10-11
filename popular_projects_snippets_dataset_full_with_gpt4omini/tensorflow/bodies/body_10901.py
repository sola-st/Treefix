# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_test.py
if not test_util.is_gpu_available():
    self.skipTest("No GPU available")
with ops.Graph().as_default() as g:
    with g.device("/device:CPU:0"):
        x = constant(1.0, shape=[1, 1])
        y = constant(1.0, shape=[1, 1])
        s = x + y
    with g.device("/device:GPU:0"):
        z = math_ops.reduce_sum(s)

    gz_x = gradients.gradients(z, [x], colocate_gradients_with_ops=True,
                               gate_gradients=True)[0]

    # Make sure the placer doesn't complain.
    self.evaluate(gz_x)
