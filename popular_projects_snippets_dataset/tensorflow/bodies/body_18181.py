# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# out = x @ y @ y @ y @ y, where @ is matmul operator.
_, out = control_flow_ops.while_loop(
    lambda i, _: i < 4, lambda i, out: (i + 1, math_ops.matmul(out, y)),
    [0, x])

def loop_fn(i):
    out_i = array_ops.gather(out, i, axis=1)
    grad = gradient_ops.gradients(out_i, x)
    exit(array_ops.reshape(grad[0], [-1]))

if use_pfor:
    exit(pfor_control_flow_ops.pfor(loop_fn, iters=3))
else:
    exit(pfor_control_flow_ops.for_loop(
        loop_fn, iters=3, loop_fn_dtypes=out.dtype))
