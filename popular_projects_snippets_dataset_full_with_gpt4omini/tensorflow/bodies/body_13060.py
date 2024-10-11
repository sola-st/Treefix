# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
"""With accidental hit removal, no subtract_log_q."""
np.random.seed(0)
num_classes = 5
batch_size = 3
sampled = [1, 0, 2, 3]

for num_true in range(1, 5):
    labels = np.random.randint(
        low=0, high=num_classes, size=batch_size * num_true)
    (weights, biases, hidden_acts, sampled_vals, _,
     _) = self._GenerateTestData(
         num_classes=num_classes,
         dim=10,
         batch_size=batch_size,
         num_true=num_true,
         labels=labels,
         sampled=sampled,
         subtract_log_q=False)
    logits_tensor, _ = _compute_sampled_logits(
        weights=constant_op.constant(weights),
        biases=constant_op.constant(biases),
        labels=constant_op.constant(
            labels, dtype=dtypes.int64, shape=(batch_size, num_true)),
        inputs=constant_op.constant(hidden_acts),
        num_sampled=len(sampled),
        num_classes=num_classes,
        num_true=num_true,
        sampled_values=sampled_vals,
        subtract_log_q=False,
        remove_accidental_hits=True,
        partition_strategy="div",
        name="sampled_logits_accidental_hit_removal_num_true_%d" % num_true)
    # Test that the exponentiated logits of accidental hits are near 0.
    # First we need to find the hits in this random test run:
    labels_reshape = labels.reshape((batch_size, num_true))
    got_logits = self.evaluate(logits_tensor)
    for row in range(batch_size):
        row_labels = labels_reshape[row, :]
        for col in range(len(sampled)):
            if sampled[col] in row_labels:
                # We need to add the num_true_test offset into logits_*
                self.assertNear(
                    np.exp(got_logits[row, col + num_true]), 0., self._eps)
