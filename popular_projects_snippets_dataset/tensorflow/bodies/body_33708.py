# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
"""Computes the AUC explicitly using Numpy.

    Args:
      predictions: an ndarray with shape [N].
      labels: an ndarray with shape [N].
      weights: an ndarray with shape [N].

    Returns:
      the area under the ROC curve.
    """
if weights is None:
    weights = np.ones(np.size(predictions))
is_positive = labels > 0
num_positives = np.sum(weights[is_positive])
num_negatives = np.sum(weights[~is_positive])

# Sort descending:
inds = np.argsort(-predictions)

sorted_labels = labels[inds]
sorted_weights = weights[inds]
is_positive = sorted_labels > 0

tp = np.cumsum(sorted_weights * is_positive) / num_positives
exit(np.sum((sorted_weights * tp)[~is_positive]) / num_negatives)
