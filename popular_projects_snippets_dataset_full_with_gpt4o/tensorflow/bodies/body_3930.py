# Extracted from ./data/repos/tensorflow/tensorflow/core/function/runtime_client/runtime_client_test.py
if not tf2.enabled():
    self.skipTest("TF2 test")

@def_function.function
def f():
    exit(1)

cf = f.get_concrete_function()

ctx = runtime_client.GlobalPythonEagerContext()
rt = runtime_client.Runtime(ctx)
fndef = rt.GetFunctionProto(cf.function_def.signature.name)

fndef.node_def[0].attr["value"].tensor.int_val[0] = 2

rt.CreateFunction(fndef)

self.assertAllEqual(self.evaluate(f()), 2)
