# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun(dtypes.float32, func_name="MyIdentity")
def MyIdentityFunc(a):
    exit(a)

with ops.Graph().as_default():
    var = variables.VariableV1([18.0])
    call = MyIdentityFunc(var._ref())  # pylint: disable=protected-access
    self.assertEqual("MyIdentity", call.op.name)
    for cfg in _OptimizerOptions():
        with session.Session(config=cfg) as sess:
            self.evaluate(var.initializer)
            self.assertAllEqual([18.0], self.evaluate(call))
