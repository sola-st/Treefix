# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    v = variables.VariableV1([1, 2])
    w = variables.VariableV1([3, 4])
    _ = v, w
    inited = variables.assert_variables_initialized()
    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        self.evaluate(inited)
    self.evaluate(variables.global_variables_initializer())
    self.evaluate(inited)
