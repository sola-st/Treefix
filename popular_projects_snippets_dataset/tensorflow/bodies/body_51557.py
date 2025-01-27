# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = checkpoint.Checkpoint()
root.v = variables.Variable(2.0)
root.f = def_function.function(lambda x: root.v * x)
root.g = def_function.function(root.f)
for _ in range(cycles):
    with backprop.GradientTape() as tape:
        inp = constant_op.constant(2.0)
        tape.watch(inp)
        output = root.g(inp)
        self.assertAllClose(4.0, output)
    self.assertAllClose(2.0, tape.gradient(output, inp))
    root = cycle(root, 1, use_cpp_bindings=use_cpp_bindings)
