# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softmax_op_test.py
# Make sure that we properly handle large inputs. See
# https://github.com/tensorflow/tensorflow/issues/4425 for details
for dims in [129, 256]:
    ones = np.random.rand(dims, dims).astype(np.float32)
    np_softmax = self._npSoftmax(ones)

    for use_gpu in [True, False]:
        with self.cached_session(use_gpu=use_gpu):
            x = constant_op.constant(ones)
            y = nn_ops.softmax(x)
            tf_softmax = self.evaluate(y)
        self.assertAllClose(tf_softmax, np_softmax)
