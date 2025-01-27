# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with self.cached_session() as sess:
    array = variables.VariableV1(
        initial_value=array_ops.zeros((0,), dtype=dtypes.string),
        name="foo",
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES])
    self.evaluate(variables.local_variables_initializer())
    old_value = array.value()
    copy_op = array.assign(old_value)
    self.assertEqual([], list(self.evaluate(copy_op)))
