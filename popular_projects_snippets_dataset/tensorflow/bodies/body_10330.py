# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
# The remapper grappler pass previously did not properly handle a 5D
# inference FusedBatchNorm followed by Relu. This asserts that this case is
# correctly handled.
np.random.seed(1)
x = np.random.random_sample((2, 3, 2, 2, 3)).astype(np.float32)
scale = np.random.random_sample((3,)).astype(np.float32)
offset = np.random.random_sample((3,)).astype(np.float32)
mean = np.random.random_sample((3,)).astype(np.float32)
var = np.random.random_sample((3,)).astype(np.float32)

epsilon = 0.001
y, _, _ = nn_impl.fused_batch_norm(
    x,
    scale,
    offset,
    mean=mean,
    variance=var,
    epsilon=epsilon,
    data_format='NCDHW',
    is_training=False)
y = nn_ops.relu(y)
y_val = self.evaluate(y)
y_ref = self._inference_ref(x, scale, offset, mean, var, epsilon,
                            'NCDHW')
y_ref = np.maximum(y_ref, 0.)
self.assertAllClose(y_ref, y_val, atol=1e-3)
