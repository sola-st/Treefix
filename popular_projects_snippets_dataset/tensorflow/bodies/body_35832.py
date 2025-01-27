# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variables_test.py
with ops.Graph().as_default(), self.cached_session() as sess:
    v = variables.VariableV1([1, 2])
    w = variables.VariableV1([3, 4])
    inited = variables.assert_variables_initialized([v])
    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        inited.op.run()
    self.evaluate(w.initializer)
    with self.assertRaisesOpError("Attempting to use uninitialized value"):
        inited.op.run()
    self.evaluate(v.initializer)
    inited.op.run()
