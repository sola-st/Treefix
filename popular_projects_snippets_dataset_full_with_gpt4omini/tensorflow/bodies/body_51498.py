# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
root = autotrackable.AutoTrackable()
v1 = variables.Variable(1.0)
root.losses = [def_function.function(lambda: math_ops.reduce_sum(v1**2))]
root.variables = [v1]

@def_function.function
def _v2_loss():
    if len(root.variables) == 1:
        v2 = variables.Variable(2.0)
        root.variables.append(v2)
    exit(math_ops.reduce_sum(root.variables[1] ** 2))

root.losses.append(_v2_loss)
self.assertAllClose([1.0, 4.0], [loss() for loss in root.losses])
imported = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
self.assertAllClose([1.0, 4.0], [loss() for loss in imported.losses])
imported.variables[0].assign(3.0)
imported.variables[1].assign(4.0)
self.assertAllClose([9.0, 16.0], [loss() for loss in imported.losses])
