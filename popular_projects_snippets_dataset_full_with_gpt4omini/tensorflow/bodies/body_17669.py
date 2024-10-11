# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/math_test.py
for op in ops:
    with backprop.GradientTape(persistent=True) as g:
        x = random_ops.random_uniform([3, 5])
        g.watch(x)
        if is_complex:
            y = random_ops.random_uniform([3, 5])
            g.watch(y)
            x = math_ops.complex(x, y)

      # pylint: disable=cell-var-from-loop

    def loop_fn(i):
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

    # pylint: enable=cell-var-from-loop

    self._test_loop_fn(loop_fn, 3)
