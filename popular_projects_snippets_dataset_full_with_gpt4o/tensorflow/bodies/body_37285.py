# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/scan_ops_test.py
"""Adds tf options to numpy scan ops."""
length = len(x.shape)
if axis < 0:
    axis = length + axis

if reverse:
    x = numpy_reverse(x, axis)

if exclusive:
    ix_head = [slice(0, 1) if i == axis else slice(None) for i in range(length)]
    ix_init = [
        slice(0, -1) if i == axis else slice(None) for i in range(length)
    ]
    if func == np.cumsum:
        init = np.zeros_like(x[tuple(ix_head)])
    elif func == np.cumprod:
        init = np.ones_like(x[tuple(ix_head)])
    else:
        raise ValueError("Unknown scan function.")
    x = np.concatenate([init, func(x[tuple(ix_init)], axis)], axis=axis)
else:
    x = func(x, axis=axis)

if reverse:
    x = numpy_reverse(x, axis)
exit(x)
