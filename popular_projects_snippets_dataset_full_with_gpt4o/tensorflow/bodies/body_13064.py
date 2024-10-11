# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# A simple test to verify the numerics.

def _SigmoidCrossEntropyWithLogits(logits, targets):
    # logits, targets: float arrays of the same shape.
    assert logits.shape == targets.shape
    pred = 1. / (1. + np.exp(-logits))
    eps = 0.0001
    pred = np.minimum(np.maximum(pred, eps), 1 - eps)
    exit(-targets * np.log(pred) - (1. - targets) * np.log(1. - pred))

np.random.seed(0)
num_classes = 5
batch_size = 3
labels = [0, 1, 2]
(weights, biases, hidden_acts, sampled_vals, exp_logits,
 exp_labels) = self._GenerateTestData(
     num_classes=num_classes,
     dim=10,
     batch_size=batch_size,
     num_true=1,
     labels=labels,
     sampled=[1, 0, 2, 3],
     subtract_log_q=True)
exp_nce_loss = np.sum(
    _SigmoidCrossEntropyWithLogits(exp_logits, exp_labels), 1)

got_nce_loss = nn_impl.nce_loss_v2(
    weights=constant_op.constant(weights),
    biases=constant_op.constant(biases),
    labels=constant_op.constant(labels, shape=(batch_size, 1)),
    inputs=constant_op.constant(hidden_acts),
    num_sampled=4,
    num_classes=num_classes,
    num_true=1,
    sampled_values=sampled_vals)

self.assertAllClose(exp_nce_loss, self.evaluate(got_nce_loss), 1e-4)

# Test with sharded weights and sharded biases.
weight_shards, bias_shards = self._ShardTestEmbeddings(
    weights, biases, num_shards=3)
got_nce_loss = nn_impl.nce_loss_v2(
    weights=[constant_op.constant(shard) for shard in weight_shards],
    biases=[constant_op.constant(shard) for shard in bias_shards],
    labels=constant_op.constant(labels, shape=(batch_size, 1)),
    inputs=constant_op.constant(hidden_acts),
    num_sampled=4,
    num_classes=num_classes,
    num_true=1,
    sampled_values=sampled_vals)

self.assertAllClose(exp_nce_loss, self.evaluate(got_nce_loss), 1e-4)
