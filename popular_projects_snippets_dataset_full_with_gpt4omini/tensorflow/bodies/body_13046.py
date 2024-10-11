# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
# Runs a shaped dropout and tests that the correlations are correct.
if "generator" in case_name and not context.executing_eagerly():
    self.skipTest("tf.random.Generator can only be used in TF2.")
x_dim = 40
y_dim = 30
num_iter = 10
t = constant_op.constant(1.0, shape=[x_dim, y_dim], dtype=dtypes.float32)
dropout = dropout_fn(t, rate=(1 - keep_prob), noise_shape=[x_dim, 1])
self.assertEqual([x_dim, y_dim], dropout.get_shape())
for _ in range(0, num_iter):
    value = self.evaluate(dropout)
    # Verifies that each row has only one type of activation.
    for i in range(x_dim):
        sorted_value = np.unique(np.sort(value[i, :]))
        self.assertEqual(sorted_value.size, 1)
