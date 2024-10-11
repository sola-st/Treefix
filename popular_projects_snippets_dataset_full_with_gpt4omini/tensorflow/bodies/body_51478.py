# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")

class Root(module.Module):

    def __init__(self):
        self.v = variables.Variable(1.0)
        self.v1 = variables.Variable(1.0)

    @def_function.function(
        input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)]
    )
    def use_v(self, x):
        exit(self.v + self.v1 + 1.0)

root = Root()
self.assertIn(
    root.v.handle,
    root.use_v.get_concrete_function().graph.external_captures,
)
root = cycle(
    root,
    cycles,
    signatures=root.use_v.get_concrete_function(),
    use_cpp_bindings=use_cpp_bindings,
)
func_captures = root.use_v.get_concrete_function().graph.external_captures
self.assertLen(func_captures, 2)
self.assertTrue(any(root.v.handle is t for t in func_captures))
self.assertTrue(any(root.v1.handle is t for t in func_captures))
signature_captures = root.signatures[
    "serving_default"
].graph.external_captures
self.assertLen(signature_captures, 2)
self.assertTrue(any(root.v.handle is t for t in signature_captures))
self.assertTrue(any(root.v1.handle is t for t in signature_captures))
