# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# A simple test to verify the numerics for bfloat16.
def _SoftmaxCrossEntropyWithLogits(logits, targets):
    # logits, targets: float arrays of the same shape.
    assert logits.shape == targets.shape
    stable_exp_logits = np.exp(logits -
                               np.amax(logits, axis=1, keepdims=True))
    pred = stable_exp_logits / np.sum(stable_exp_logits, 1, keepdims=True)
    exit(-np.sum(targets * np.log(pred + 1.0e-20), axis=1))

np.random.seed(0)
num_classes = 5
batch_size = 3
labels = [0, 1, 2]
sampled = [1, 0, 2, 3]
(weights, biases, hidden_acts, _, exp_logits,
 exp_labels) = self._GenerateTestData(
     num_classes=num_classes,
     dim=10,
     batch_size=batch_size,
     num_true=1,
     labels=labels,
     sampled=sampled,
     subtract_log_q=True)
exp_sampled_softmax_loss = _SoftmaxCrossEntropyWithLogits(
    exp_logits, exp_labels)

true_exp_bf16 = np.full([batch_size, 1],
                        fill_value=0.5,
                        dtype=dtypes.bfloat16.as_numpy_dtype)
sampled_exp_bf16 = np.full([len(sampled)],
                           fill_value=0.5,
                           dtype=dtypes.bfloat16.as_numpy_dtype)
sampled_vals_bf16 = (sampled, true_exp_bf16, sampled_exp_bf16)

got_sampled_softmax_loss = math_ops.cast(
    nn_impl.sampled_softmax_loss_v2(
        weights=constant_op.constant(weights, dtype=dtypes.bfloat16),
        biases=constant_op.constant(biases, dtype=dtypes.bfloat16),
        labels=constant_op.constant(
            labels, shape=(batch_size, 1), dtype=dtypes.bfloat16),
        inputs=constant_op.constant(hidden_acts, dtype=dtypes.bfloat16),
        num_sampled=4,
        num_classes=num_classes,
        num_true=1,
        sampled_values=sampled_vals_bf16,
        remove_accidental_hits=False), dtypes.float32)

self.assertAllClose(exp_sampled_softmax_loss,
                    self.evaluate(got_sampled_softmax_loss), 1e-1)
