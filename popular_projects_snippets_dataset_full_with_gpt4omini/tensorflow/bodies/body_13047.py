# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# Runs dropout with 0-1 tensor 10 times, sum the number of ones and validate
# that it is producing approximately the right number of ones over a large
# number of samples, based on the keep probability.
if use_keep_prob and case_name != "stateful_v1":
    self.skipTest("Only V1 `dropout` has the `keep_prob` argument.")
if "generator" in case_name and not context.executing_eagerly():
    self.skipTest("tf.random.Generator can only be used in TF2.")
x_dim = 70
y_dim = 30
num_iter = 10
t = constant_op.constant(
    1.0, shape=[x_dim, y_dim], dtype=dtypes.float32)
final_count = 0
for _ in range(0, num_iter):
    if use_keep_prob:
        dropout = dropout_fn(t, keep_prob=keep_prob)
    else:
        dropout = dropout_fn(t, rate=1 - keep_prob)
    self.assertEqual([x_dim, y_dim], dropout.get_shape())
    value = self.evaluate(dropout)
    final_count += np.count_nonzero(value)
    # Verifies that there are only two values: 0 and 1/keep_prob.
    sorted_value = np.unique(np.sort(value))
    self.assertEqual(0, sorted_value[0])
    self.assertAllClose(1 / keep_prob, sorted_value[1])
# Check that we are in the 15% error range
expected_count = x_dim * y_dim * keep_prob * num_iter
rel_error = math.fabs(final_count - expected_count) / expected_count
self.assertLess(rel_error, 0.15)
