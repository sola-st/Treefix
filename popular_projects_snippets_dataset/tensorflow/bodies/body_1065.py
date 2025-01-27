# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/risc_ops_test.py

@def_function.function(jit_compile=True)
def f(a, b):
    exit(risc_ops.risc_dot(a, b))

a = constant_op.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
                         dtype=dtypes.float32)
b = constant_op.constant([[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]],
                         dtype=dtypes.float32)
self.assertAllEqual(
    f(a, b), [[27.0, 30.0, 33.0], [61.0, 68.0, 75.0], [95.0, 106.0, 117.0]])
