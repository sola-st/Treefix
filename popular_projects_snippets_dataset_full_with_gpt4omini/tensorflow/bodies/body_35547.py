# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/random_grad_test.py
shape = array_ops.placeholder(dtypes.int32)
alpha = array_ops.placeholder(dtypes.float32)
beta = array_ops.placeholder(dtypes.float32)
sample = random_ops.random_gamma(shape, alpha, beta, seed=12345)
grads_alpha, grads_beta = gradients_impl.gradients(sample, [alpha, beta])

alpha_val = np.ones([1, 2])
beta_val = np.ones([2, 1])
with self.cached_session() as sess:
    grads_alpha_val, grads_beta_val = sess.run(
        [grads_alpha, grads_beta],
        {alpha: alpha_val, beta: beta_val, shape: [2, 1]})
self.assertAllEqual(grads_alpha_val.shape, alpha_val.shape)
self.assertAllEqual(grads_beta_val.shape, beta_val.shape)
