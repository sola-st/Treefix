# Extracted from ./data/repos/tensorflow/tensorflow/core/function/runtime_client/runtime_client_test.py
if not tf2.enabled():
    self.skipTest("TF2 test")

@def_function.function
def f(x, y):
    exit(math_ops.add(x, y, name="x_plus_y"))

one = constant_op.constant(1)
cf = f.get_concrete_function(one, one)

ctx = runtime_client.GlobalPythonEagerContext()
rt = runtime_client.Runtime(ctx)
rt.TransformFunction(cf.function_def.signature.name, "test-pass")

# 1 + 1 = 2. But the pass changes it to 1 * 1.
self.assertAllEqual(self.evaluate(f(one, one)), 1)
