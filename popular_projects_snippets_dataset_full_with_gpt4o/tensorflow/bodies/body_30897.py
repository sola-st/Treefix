# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
features = [[1., 1., 1., 1.], [1., 2., 3., 4.]]
# Batch 0: All exps are 1.  The expected result is
# Softmaxes = [0.25, 0.25, 0.25, 0.25]
# LogSoftmaxes = [-1.386294, -1.386294, -1.386294, -1.386294]
#
# Batch 1:
# exps = [1., 2.718, 7.389, 20.085]
# sum = 31.192
# Softmaxes = exps / sum = [0.0320586, 0.08714432, 0.23688282, 0.64391426]
# LogSoftmaxes = [-3.44019 , -2.44019 , -1.44019 , -0.44019]
np_sm = self._npSoftmax(np.array(features))
self.assertAllClose(
    np.array([[0.25, 0.25, 0.25, 0.25],
              [0.0320586, 0.08714432, 0.23688282, 0.64391426]]),
    np_sm,
    rtol=1.e-5,
    atol=1.e-5)
np_lsm = self._npSoftmax(np.array(features), log=True)
self.assertAllClose(
    np.array([[-1.386294, -1.386294, -1.386294, -1.386294],
              [-3.4401897, -2.4401897, -1.4401897, -0.4401897]]),
    np_lsm,
    rtol=1.e-5,
    atol=1.e-5)
