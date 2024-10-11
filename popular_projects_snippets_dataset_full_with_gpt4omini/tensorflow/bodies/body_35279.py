# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/categorical_test.py
with self.cached_session():
    logits = array_ops.placeholder(dtype=dtypes.float32)
    dist = categorical.Categorical(logits)
    sample = dist.sample()
    # Will sample class 1.
    sample_value = sample.eval(feed_dict={logits: [-1000.0, 1000.0]})
    self.assertEqual(1, sample_value)

    # Batch entry 0 will sample class 1, batch entry 1 will sample class 0.
    sample_value_batch = sample.eval(
        feed_dict={logits: [[-1000.0, 1000.0], [1000.0, -1000.0]]})
    self.assertAllEqual([1, 0], sample_value_batch)
