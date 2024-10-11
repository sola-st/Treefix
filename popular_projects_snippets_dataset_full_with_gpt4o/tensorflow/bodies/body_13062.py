# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
"""With sharded weights and sharded biases."""
np.random.seed(0)
num_classes = 5
batch_size = 3

for num_true in range(1, 5):
    labels = np.random.randint(
        low=0, high=num_classes, size=batch_size * num_true)
    (weights, biases, hidden_acts, sampled_vals, exp_logits,
     exp_labels) = self._GenerateTestData(
         num_classes=num_classes,
         dim=10,
         batch_size=batch_size,
         num_true=num_true,
         labels=labels,
         sampled=[1, 0, 2, 3],
         subtract_log_q=False)
    weight_shards, bias_shards = self._ShardTestEmbeddings(
        weights, biases, num_shards=3)
    logits_tensor, labels_tensor = _compute_sampled_logits(
        weights=[constant_op.constant(shard) for shard in weight_shards],
        biases=[constant_op.constant(shard) for shard in bias_shards],
        labels=constant_op.constant(
            labels, dtype=dtypes.int64, shape=(batch_size, num_true)),
        inputs=constant_op.constant(hidden_acts),
        num_sampled=4,
        num_classes=num_classes,
        num_true=num_true,
        sampled_values=sampled_vals,
        subtract_log_q=False,
        remove_accidental_hits=False,
        partition_strategy="div",
        name="sampled_logits_sharded_num_true_%d" % num_true)
    got_logits, got_labels = self.evaluate([logits_tensor, labels_tensor])
    self.assertAllClose(exp_logits, got_logits, self._eps)
    self.assertAllClose(exp_labels, got_labels, self._eps)
