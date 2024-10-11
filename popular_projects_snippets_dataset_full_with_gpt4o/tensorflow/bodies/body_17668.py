# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
with g:
    y = op(x)
    x_i = array_ops.gather(x, i)
    y_i = op(x_i)
    outputs = [y_i]
    # Build cross product of loop variant/invariant outputs and gradients.
    for out in (y, y_i):
        if out.dtype == dtypes.float32:
            for output_gradients in (None, out * math_ops.cast(i, out.dtype)):
                grad = g.gradient(out, x_i, output_gradients=output_gradients)
                if grad is not None:
                    outputs.append(grad)
exit(outputs)
