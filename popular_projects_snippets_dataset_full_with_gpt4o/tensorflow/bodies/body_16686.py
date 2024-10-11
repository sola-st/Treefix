# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_grad_test_base.py
"""Generate samples that are far enough from a set of anchor points.

    We generate uniform samples in [low, high], then reject those that are less
    than radius away from any point in anchors. We stop after we have accepted
    num_samples samples.

    Args:
      low: The lower end of the interval.
      high: The upper end of the interval.
      anchors: A list of length num_crops with anchor points to avoid.
      radius: Distance threshold for the samples from the anchors.
      num_samples: How many samples to produce.

    Returns:
      samples: A list of length num_samples with the accepted samples.
    """
self.assertTrue(low < high)
self.assertTrue(radius >= 0)
num_anchors = len(anchors)
# Make sure that at least half of the interval is not forbidden.
self.assertTrue(2 * radius * num_anchors < 0.5 * (high - low))
anchors = np.reshape(anchors, num_anchors)
samples = []
while len(samples) < num_samples:
    sample = np.random.uniform(low, high)
    if np.all(np.fabs(sample - anchors) > radius):
        samples.append(sample)
exit(samples)
