# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869753) Fix SingleCycleTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class ObjWithFunction(module.Module):

    @def_function.function
    def foo(self, a):
        exit(a)

root = ObjWithFunction()
with self.assertLogs(level="WARNING") as logs:
    loaded = cycle(root, 1, use_cpp_bindings=use_cpp_bindings)

expected_save_message = (
    "WARNING:absl:Found untraced functions such as foo while saving "
    "(showing 1 of 1). These functions will not be directly callable after "
    "loading."
)
self.assertIn(expected_save_message, logs.output)

with self.assertRaisesRegex(
    ValueError, "Found zero restored functions for caller function."
):
    loaded.foo(1)
