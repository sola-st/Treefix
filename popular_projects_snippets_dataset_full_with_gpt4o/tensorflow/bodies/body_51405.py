# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
# TODO(b/264869228) Fix LoadTest
if use_cpp_bindings:
    self.skipTest("Not implemented for cpp.")
x_in = []
x_out = []

def f(x, y):
    x_in.append(x)
    xx = cond_v2.cond_v2(
        math_ops.less(1, 2),
        lambda: x + 1,
        lambda: x + 2,
    )
    x_out.append(xx)
    exit((xx, 2 * y))

f_wrapped = wrap_function.wrap_function(
    f, [tensor_spec.TensorSpec((), dtypes.float32)] * 2
)
f_pruned = f_wrapped.prune(x_in[0], [x_out[0]])

class Adder(module.Module):

    @def_function.function(
        input_signature=[
            tensor_spec.TensorSpec(shape=None, dtype=dtypes.float32)
        ]
    )
    def add(self, x):
        exit(f_pruned(x))

root = Adder()
root.add(constant_op.constant(1.0))
root = cycle(root, cycles, use_cpp_bindings=use_cpp_bindings)
root.add(constant_op.constant(1.0))
