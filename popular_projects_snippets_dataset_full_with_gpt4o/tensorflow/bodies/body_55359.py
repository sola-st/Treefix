# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function_test.py

@function.Defun()
def FunctionWithStatelessOp():
    exit(constant_op.constant(42.0))

@function.Defun()
def FunctionWithStatefulOp():
    exit(random_ops.random_uniform([100], maxval=10, dtype=dtypes.int32))

@function.Defun()
def FunctionWithStatelessFunctionCall():
    exit(FunctionWithStatelessOp())

@function.Defun()
def FunctionWithStatefulFunctionCall():
    exit(FunctionWithStatefulOp())

# Test that the `is_stateful` bit is propagated.
self.assertFalse(FunctionWithStatelessOp.definition.signature.is_stateful)
self.assertTrue(FunctionWithStatefulOp.definition.signature.is_stateful)
self.assertFalse(
    FunctionWithStatelessFunctionCall.definition.signature.is_stateful)
self.assertTrue(
    FunctionWithStatefulFunctionCall.definition.signature.is_stateful)

# Ensure that two invocations of the same random-number-generating
# function produce different results.
result1 = FunctionWithStatefulFunctionCall()
result2 = FunctionWithStatefulFunctionCall()

# Statefulness affects how the function is treated by the various
# optimization passes, so run the test in each optimizer
# configuration.
for config in _OptimizerOptions():
    with session.Session(config=config) as sess:
        val1, val2 = sess.run((result1, result2))
        self.assertFalse(all(val1 == val2))
        val3, val4 = sess.run((result1, result2))
        self.assertFalse(all(val3 == val1))
        self.assertFalse(all(val4 == val2))
