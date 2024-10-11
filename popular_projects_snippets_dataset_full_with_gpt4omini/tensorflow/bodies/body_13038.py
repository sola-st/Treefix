# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
for dtype in [dtypes.float32, dtypes.float64] + \
                 [dtypes.bfloat16] if test_util.is_gpu_available(
                                      cuda_only=True) else []:
    x = constant_op.constant([1.0, 0.0, 3.0, 2.0],
                             shape=[2, 2],
                             name="x",
                             dtype=dtype)
    l2loss = nn_ops.l2_loss(x)
    value = self.evaluate(l2loss)
    self.assertAllClose(7.0, value)
