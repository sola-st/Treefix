# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
"""Test catching Infinity caused by overflow in a tf.function with while."""
check_numerics_callback.enable_check_numerics()

@def_function.function
def accumulation_function(counter, lim, accum):
    while math_ops.less(counter, lim):
        accum.assign(accum * 2.0)
        counter.assign_add(1)

counter = variables.Variable(0, dtype=dtypes.int32)
# Repeated `* 2.0` overflows a float32 tensor in 128 steps. So the
# 1000-step limit is sufficient.
lim = constant_op.constant(1000, dtype=dtypes.int32)
accum = variables.Variable(1.0)

if not context.executing_eagerly():
    self.evaluate([counter.initializer, accum.initializer])

message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
    lambda: self.evaluate(accumulation_function(counter, lim, accum)))

self.assertAllClose(self.evaluate(counter), 128)
# Check the content of the error message.
# The overflow to +Infinity happens during the `* 2.0` operation.
self.assertTrue(re.search(r"graph op.*\"Mul\"", message))
self.assertTrue(re.search(r"dtype.*float32", message))
self.assertIn("shape: ()\n", message)
# Check that the correct input op is printed.
self.assertIn("Input tensors (2):", message)
# Check that the correct input ops are printed.
self.assertTrue(re.search(r"0:.*Tensor.*ReadVariableOp:0", message))
self.assertTrue(re.search(r"1:.*Tensor.*mul/y:0", message))
# Check that the correct line for op creation is printed.
self.assertTrue(re.search(r"Stack trace of op's creation", message))
self.assertIn("accum.assign(accum * 2.0)", message)
