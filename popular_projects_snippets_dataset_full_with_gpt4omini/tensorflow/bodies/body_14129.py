# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
"""Test when the rank is unknown."""

@def_function.function
def my_fun(foo):
    bar_shape = math_ops.range(foo)
    bar = array_ops.zeros(shape=bar_shape)
    structured_array_ops._structured_tensor_like(bar)

with self.assertRaisesRegex(ValueError,
                            "Can't build StructuredTensor w/ unknown rank"):
    my_fun(array_ops.constant(3))
