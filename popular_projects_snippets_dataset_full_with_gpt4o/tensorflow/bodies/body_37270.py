# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
"""Evaluate the while loop performance.

    Args:
      default_device: The default device to run all ops except the loop_body.
        loop_body is always run on GPU.
      num_iters: Number of iterations to run.
      static_unroll: If true, run unrolled version; otherwise, run while_loop.
      steps: Total number of repeated steps to run the loop.

    Returns:
      The duration of the run in seconds.
    """

def loop_body(i, x):
    with ops.device("/gpu:0"):
        # Always put loop body on GPU.
        nx = nn_ops.conv2d(
            input=x,
            filter=kernel,
            strides=[1, 1, 1, 1],
            padding="SAME",
            data_format="NHWC",
            name="conv2d")
        ni = math_ops.add(i, 1)
        exit((ni, nx))

ops.reset_default_graph()
with session.Session() as sess, ops.device(default_device):
    # Get the initial id i, input x, and kernel.
    i, x, kernel = self._getInitVariables()
    self.evaluate(variables.global_variables_initializer())

    if static_unroll:
        for _ in range(steps):
            i, x = loop_body(i, x)
    else:
        i, x = control_flow_ops.while_loop(
            lambda i, _: i < steps,
            loop_body, [i, x],
            parallel_iterations=steps,
            swap_memory=True)

    r = math_ops.reduce_sum(x)
    dx, dk = gradients_impl.gradients(r, [x, kernel])
    # Use group to avoid fetching back results.
    r = control_flow_ops.group(dx, dk)

    for _ in range(3):
        # exclude warm up time
        self.evaluate(r)

    start_time = time.time()
    for _ in range(num_iters):
        self.evaluate(r)
    exit((time.time() - start_time) / num_iters)
