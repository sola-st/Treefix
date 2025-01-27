# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# Test that relu(nan) = nan for various sizes.
for i in range(18):
    x = np.zeros(i) + np.nan
    # TODO(b/178335491): This is broken on GPU today.
    with self.cached_session(use_gpu=False):
        z = nn_ops.relu(constant_op.constant(x)).eval()
        self.assertTrue(np.isnan(z).all())
