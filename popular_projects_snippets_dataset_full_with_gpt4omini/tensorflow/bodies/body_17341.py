# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Test case for GitHub issue 28241."""
image = np.random.random([512, 512, 1])
score_tensor = image_ops.ssim_multiscale(image, image, max_val=1.0)
with self.cached_session():
    _ = self.evaluate(score_tensor)
