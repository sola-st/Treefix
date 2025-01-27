# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util_test.py
with ops.Graph().as_default() as g:
    self.assertIsNone(training_util.get_global_step())
    variables.VariableV1(
        0,
        trainable=False,
        dtype=dtypes.int32,
        name=ops.GraphKeys.GLOBAL_STEP,
        collections=[ops.GraphKeys.GLOBAL_STEP])
    self._assert_global_step(
        training_util.get_global_step(), expected_dtype=dtypes.int32)
self._assert_global_step(
    training_util.get_global_step(g), expected_dtype=dtypes.int32)
