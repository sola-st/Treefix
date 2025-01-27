# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/pad_op_test.py
np_val = self._npPad(np_inputs, paddings, mode=mode,
                     constant_values=constant_values)
for use_gpu in [True, False]:
    with test_util.device(use_gpu=use_gpu):
        tf_val = array_ops.pad(np_inputs, paddings, mode=mode,
                               constant_values=constant_values)
        out = self.evaluate(tf_val)

        if np_inputs.dtype in [self._qint8, self._quint8, self._qint32]:
            # Cast quantized types back to their numpy equivalents.
            np_val = np_val.astype(np_inputs.dtype[0])

    self.assertAllEqual(np_val, out)
    self.assertShapeEqual(np_val, tf_val)
