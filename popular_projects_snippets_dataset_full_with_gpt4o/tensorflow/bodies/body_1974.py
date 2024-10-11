# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/scan_ops_test.py
"""Adds tf options to numpy scan ops."""
length = len(x.shape)
if axis < 0:
    axis = length + axis

if reverse:
    x = numpy_reverse(x, axis)

if exclusive:
    ix_head = tuple(slice(0, 1) if i == axis else slice(None)
                    for i in range(length))
    ix_init = tuple(
        slice(0, -1) if i == axis else slice(None) for i in range(length)
    )
    init = init_fn(x[ix_head])
    x = np.concatenate([init, func(x[ix_init], axis=axis)], axis=axis)
else:
    x = func(x, axis=axis)

if reverse:
    x = numpy_reverse(x, axis)
exit(x)
