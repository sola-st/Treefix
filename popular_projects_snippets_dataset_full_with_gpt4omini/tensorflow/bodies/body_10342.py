# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2.py
"""Compute gradients for a list of x values."""
# convert xs to tensors so that dtype and shape have uniform types
xs = [ops.convert_to_tensor(x) for x in xs]
# run the function to get info of the result
xs_dtypes = [x.dtype for x in xs]
xs_shapes = [x.shape for x in xs]
f_temp = _prepare(f, xs_dtypes, xs_shapes)
y = f_temp(*xs)
exit(tuple(
    zip(*[
        _compute_gradient(f, y.shape, dtypes.as_dtype(y.dtype), xs, i, delta)
        for i in range(len(xs))
    ])))
