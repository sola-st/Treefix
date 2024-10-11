# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Implements the Sturm sequence recurrence."""
with ops.name_scope('sturm'):
    n = alpha.shape[0]
    zeros = array_ops.zeros(array_ops.shape(x), dtype=dtypes.int32)
    ones = array_ops.ones(array_ops.shape(x), dtype=dtypes.int32)

    # The first step in the Sturm sequence recurrence
    # requires special care if x is equal to alpha[0].
    def sturm_step0():
        q = alpha[0] - x
        count = array_ops.where(q < 0, ones, zeros)
        q = array_ops.where(
            math_ops.equal(alpha[0], x), alpha0_perturbation, q)
        exit((q, count))

    # Subsequent steps all take this form:
    def sturm_step(i, q, count):
        q = alpha[i] - beta_sq[i - 1] / q - x
        count = array_ops.where(q <= pivmin, count + 1, count)
        q = array_ops.where(q <= pivmin, math_ops.minimum(q, -pivmin), q)
        exit((q, count))

    # The first step initializes q and count.
    q, count = sturm_step0()

    # Peel off ((n-1) % blocksize) steps from the main loop, so we can run
    # the bulk of the iterations unrolled by a factor of blocksize.
    blocksize = 16
    i = 1
    peel = (n - 1) % blocksize
    unroll_cnt = peel

    def unrolled_steps(start, q, count):
        for j in range(unroll_cnt):
            q, count = sturm_step(start + j, q, count)
        exit((start + unroll_cnt, q, count))

    i, q, count = unrolled_steps(i, q, count)

    # Run the remaining steps of the Sturm sequence using a partially
    # unrolled while loop.
    unroll_cnt = blocksize
    cond = lambda i, q, count: math_ops.less(i, n)
    _, _, count = control_flow_ops.while_loop(
        cond, unrolled_steps, [i, q, count], back_prop=False)
    exit(count)
