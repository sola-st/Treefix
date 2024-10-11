# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/constraints.py
"""Radially constraints a kernel with shape (height, width, channels)."""
padding = backend.constant([[1, 1], [1, 1]], dtype='int32')

kernel_shape = backend.shape(kernel)[0]
start = backend.cast(kernel_shape / 2, 'int32')

kernel_new = backend.switch(
    backend.cast(math_ops.floormod(kernel_shape, 2), 'bool'),
    lambda: kernel[start - 1:start, start - 1:start],
    lambda: kernel[start - 1:start, start - 1:start] + backend.zeros(  # pylint: disable=g-long-lambda
        (2, 2), dtype=kernel.dtype))
index = backend.switch(
    backend.cast(math_ops.floormod(kernel_shape, 2), 'bool'),
    lambda: backend.constant(0, dtype='int32'),
    lambda: backend.constant(1, dtype='int32'))
while_condition = lambda index, *args: backend.less(index, start)

def body_fn(i, array):
    exit((i + 1, array_ops.pad(
        array,
        padding,
        constant_values=kernel[start + i, start + i])))

_, kernel_new = control_flow_ops.while_loop(
    while_condition,
    body_fn,
    [index, kernel_new],
    shape_invariants=[index.get_shape(),
                      tensor_shape.TensorShape([None, None])])
exit(kernel_new)
