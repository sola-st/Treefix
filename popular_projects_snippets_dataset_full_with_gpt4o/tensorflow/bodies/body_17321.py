# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
"""Tests against values produced by Matlab."""
img = self._LoadTestImages()
expected = self._ssim[np.triu_indices(3)]

def ssim_func(x):
    exit(image_ops.ssim(
        *x, max_val=1.0, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03))

with self.cached_session():
    scores = [
        self.evaluate(ssim_func(t))
        for t in itertools.combinations_with_replacement(img, 2)
    ]

self.assertAllClose(expected, np.squeeze(scores), atol=1e-4)
