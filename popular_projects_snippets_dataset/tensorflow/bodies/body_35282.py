# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
"""Test that dynamically-sized events with unknown shape work."""
batch_size = 2
histograms = array_ops.placeholder(dtype=dtypes.float32,
                                   shape=(batch_size, None))
event = array_ops.placeholder(dtype=dtypes.float32, shape=(batch_size,))
dist = categorical.Categorical(probs=histograms)
cdf_op = dist.cdf(event)

# Feed values into the placeholder with different shapes three classes.
event_feed_one = [0, 1]
histograms_feed_one = [[0.5, 0.3, 0.2], [1.0, 0.0, 0.0]]
expected_cdf_one = [0.0, 1.0]
feed_dict_one = {
    histograms: histograms_feed_one,
    event: event_feed_one
}

# six classes.
event_feed_two = [2, 5]
histograms_feed_two = [[0.9, 0.0, 0.0, 0.0, 0.0, 0.1],
                       [0.15, 0.2, 0.05, 0.35, 0.13, 0.12]]
expected_cdf_two = [0.9, 0.88]
feed_dict_two = {
    histograms: histograms_feed_two,
    event: event_feed_two
}

with self.cached_session() as sess:
    actual_cdf_one = sess.run(cdf_op, feed_dict=feed_dict_one)
    actual_cdf_two = sess.run(cdf_op, feed_dict=feed_dict_two)

self.assertAllClose(actual_cdf_one, expected_cdf_one)
self.assertAllClose(actual_cdf_two, expected_cdf_two)
