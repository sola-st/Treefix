# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
np_val = self._npBias(np_inputs, np_bias)
np_inputs = self._NHWCToNCHW(np_inputs)
with self.cached_session(use_gpu=use_gpu):
    tf_val = self.evaluate(
        nn_ops.bias_add(np_inputs, np_bias, data_format="NCHW"))
tf_val = self._NCHWToNHWC(tf_val)
self.assertAllCloseAccordingToType(self._AtLeast3d(np_val), tf_val)
