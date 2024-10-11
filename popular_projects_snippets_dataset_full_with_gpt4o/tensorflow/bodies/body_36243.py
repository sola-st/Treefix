# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/functional_ops_test.py
# We construct a 5-layer Multi-Layer Perceptron network here.
# Each layer have the same number of hidden unites (3), and the
# activation function is tanh().  We feed the input (xval) with
# batch size 2.
xval = np.random.normal(size=(2, 3))
wsval = np.random.normal(size=(5, 3, 3))
bsval = np.random.normal(size=(5, 3))
np_ans = self._npMLP(xval, wsval, bsval)
tf_for_ans = self._tfMLP(xval, wsval, bsval, rewrite_with_while)
self.assertAllClose(np_ans, tf_for_ans)
