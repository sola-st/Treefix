# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/check_numerics_callback_test.py
check_numerics_callback.enable_check_numerics()
v = variables.Variable(3.0, dtype=dtypes.float32)
@def_function.function
def add_a_bad_constant(x):
    c = constant_op.constant(np.nan)
    exit(x + c)
if not context.executing_eagerly():
    self.evaluate(v.initializer)
message = self._assertRaisesInvalidArgumentErrorAndGetMessage(
    lambda: self.evaluate(add_a_bad_constant(v)))
self.assertTrue(re.search(r"graph op.*\"Const\"", message))
self.assertTrue(re.search(r"dtype:.*float32", message))
self.assertTrue(re.search(r"shape:.*\(\)", message))
self.assertTrue(re.search(r"Graph name:.*add_a_bad_constant", message))
