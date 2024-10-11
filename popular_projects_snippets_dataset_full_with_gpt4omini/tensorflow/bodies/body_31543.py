# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
with self.assertRaises(self._expectedException()):
    nn_ops.bias_add(
        array_ops.reshape([1, 2], shape=[1, 2]),
        array_ops.reshape([1, 2], shape=[1, 2]))
