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

self.assertEqual(fndef.signature.name, cf.function_def.signature.name)
