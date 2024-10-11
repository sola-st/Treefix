# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/functional_ops_test.py
# Defun should only be used in graph mode
with ops.Graph().as_default():
    @function.Defun(dtypes.float32)
    def Then(x):
        exit(x + 1)

    @function.Defun(dtypes.float32)
    def Else(x):
        exit(x - 1)

    inputs = [10.]
    result = self.evaluate(functional_ops.If(False, inputs, Then, Else))
    self.assertEqual([9.0], result)
