# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
"""Test that dynamically-sized events with unknown shape work."""
event_ph = array_ops.placeholder_with_default(events, shape=None)
histograms_ph = array_ops.placeholder_with_default(histograms, shape=None)
dist = categorical.Categorical(probs=histograms_ph)
cdf_op = dist.cdf(event_ph)

actual_cdf = self.evaluate(cdf_op)
self.assertAllClose(actual_cdf, expected_cdf)
