# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
"""Test a complex function that takes different argument kinds.

    tf2xla machinery that translates, compiles, and runs defuns
    classifies arguments into: compile-time constants, regular tensors,
    and resources. This test creates a function with a mix of all these
    kinds. Moreover, the order of function arguments is intentionally mixed up.

    This also tests the case when the same argument is a compile-time constant
    as well as used in an operation that normally expects its inputs to be
    in device memory - addition in this case.
    """
with self.test_scope():
    def foo(c1, r1, v1, c2, v2, r2):
        # c1 and c2 are compile-time constants
        # r1 and r2 are regular tensors
        # v1 and v2 are resource variables
        a = c1 + r1
        b = math_ops.cast(c2, dtypes.float32) + v2
        c = array_ops.slice(v1, c1, c2)
        d = r2 * v2
        exit((a, b, c, d))

    foo = def_function.function(foo)

    c1 = [0, 0]
    c2 = array_ops.ones([2], dtype=dtypes.int32)

    r1 = array_ops.ones([2])
    r2 = [[2., 2.], [3., 3.]]

    v1 = resource_variable_ops.ResourceVariable([[1., 2.], [3., 4.]])
    v2 = resource_variable_ops.ResourceVariable([[10., 20.], [30., 40.]])

    a, b, c, d = foo(c1, r1, v1, c2, v2, r2)

    self.assertAllEqual([1, 1], a.numpy())
    self.assertAllEqual([[11., 21.], [31., 41.]], b.numpy())
    self.assertAllEqual([[1.]], c.numpy())
    self.assertAllEqual([[20., 40.], [90., 120.]], d.numpy())
