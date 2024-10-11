# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/einsum_op_test.py
# This is the reverse operation of generalized traces, to be used for
# computing symbolic gradients of einsum. Note: this operation is not
# supported by np.einsum as it's only required for gradients.
r = np.random.RandomState(0)
a = r.randn(2, 2)
s = 'a->aa'
diag_a = np.diag(np.diag(a))
b = self.evaluate(gen_linalg_ops.einsum([np.diag(a)], s))
self.assertAllClose(diag_a, b, atol=1e-4, rtol=1e-4)
