# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util_test.py
with ops.Graph().as_default() as g:
    self.assertIsNone(training_util.get_global_step())
    variables.VariableV1(
        0.0,
        trainable=False,
        dtype=dtypes.float32,
        name=ops.GraphKeys.GLOBAL_STEP,
        collections=[ops.GraphKeys.GLOBAL_STEP])
    self.assertRaisesRegex(TypeError, 'does not have integer type',
                           training_util.get_global_step)
self.assertRaisesRegex(TypeError, 'does not have integer type',
                       training_util.get_global_step, g)
