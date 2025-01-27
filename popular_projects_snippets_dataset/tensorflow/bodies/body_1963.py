# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/categorical_op_test.py
"""Categorical samples from given input.

    Args:
      logits: Numpy ndarray of shape [batch_size, num_classes].
      num_samples: Int; number of samples to draw.

    Returns:
      Frequencies from sampled classes; shape [batch_size, num_classes].
    """
with self.session(), self.test_scope():
    random_seed.set_random_seed(1618)
    op = random_ops.multinomial(logits, num_samples,
                                output_dtype=dtypes.int32)
    d = self.evaluate(op)

batch_size, num_classes = logits.shape
freqs_mat = []
for i in range(batch_size):
    cnts = dict(collections.Counter(d[i, :]))

    # Requires drawn class labels be in range.
    self.assertLess(max(cnts.keys()), num_classes)
    self.assertGreaterEqual(min(cnts.keys()), 0)

    freqs = [(cnts[k] * 1. / num_samples if k in cnts else 0)
             for k in range(num_classes)]
    freqs_mat.append(freqs)

exit(freqs_mat)
