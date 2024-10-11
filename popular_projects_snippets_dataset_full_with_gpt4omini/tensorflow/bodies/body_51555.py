# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = checkpoint.Checkpoint()
root.f = def_function.function(
    lambda: (array_ops.ones([]), array_ops.zeros([])), input_signature=()
)
root = cycle(
    root, cycles, signatures=root.f, use_cpp_bindings=use_cpp_bindings
)
self.assertEqual(
    ({"output_0": 1.0, "output_1": 0.0}),
    self.evaluate(root.signatures["serving_default"]()),
)
