# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/multinomial_op_test.py
"""Samples using the supplied sampler and inputs.

    Args:
      logits: Numpy ndarray of shape [batch_size, num_classes].
      num_samples: Int; number of samples to draw.
      sampler: A sampler function that takes (1) a [batch_size, num_classes]
        Tensor, (2) num_samples and returns a [batch_size, num_samples] Tensor.

    Returns:
      Frequencies from sampled classes; shape [batch_size, num_classes].
    """
with test_util.use_gpu():
    random_seed.set_random_seed(1618)
    op = sampler(constant_op.constant(logits), num_samples)
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
