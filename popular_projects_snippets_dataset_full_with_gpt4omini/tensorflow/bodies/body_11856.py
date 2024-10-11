# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Computes all eigenvalues of a Hermitian tridiagonal matrix."""

def _sturm(alpha, beta_sq, pivmin, alpha0_perturbation, x):
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

with ops.name_scope('compute_eigenvalues'):
    if alpha.dtype.is_complex:
        alpha = math_ops.real(alpha)
        beta_sq = math_ops.real(math_ops.conj(beta) * beta)
        beta_abs = math_ops.sqrt(beta_sq)
    else:
        beta_sq = math_ops.square(beta)
        beta_abs = math_ops.abs(beta)

    # Estimate the largest and smallest eigenvalues of T using the
    # Gershgorin circle theorem.
    finfo = np.finfo(alpha.dtype.as_numpy_dtype)
    off_diag_abs_row_sum = array_ops.concat(
        [beta_abs[:1], beta_abs[:-1] + beta_abs[1:], beta_abs[-1:]], axis=0)
    lambda_est_max = math_ops.minimum(
        finfo.max, math_ops.reduce_max(alpha + off_diag_abs_row_sum))
    lambda_est_min = math_ops.maximum(
        finfo.min, math_ops.reduce_min(alpha - off_diag_abs_row_sum))
    # Upper bound on 2-norm of T.
    t_norm = math_ops.maximum(
        math_ops.abs(lambda_est_min), math_ops.abs(lambda_est_max))

    # Compute the smallest allowed pivot in the Sturm sequence to avoid
    # overflow.
    one = np.ones([], dtype=alpha.dtype.as_numpy_dtype)
    safemin = np.maximum(one / finfo.max, (one + finfo.eps) * finfo.tiny)
    pivmin = safemin * math_ops.maximum(one, math_ops.reduce_max(beta_sq))
    alpha0_perturbation = math_ops.square(finfo.eps * beta_abs[0])
    abs_tol = finfo.eps * t_norm
    if tol:
        abs_tol = math_ops.maximum(tol, abs_tol)
    # In the worst case, when the absolute tolerance is eps*lambda_est_max
    # and lambda_est_max = -lambda_est_min, we have to take as many
    # bisection steps as there are bits in the mantissa plus 1.
    max_it = finfo.nmant + 1

    # Determine the indices of the desired eigenvalues, based on select
    # and select_range.
    asserts = None
    if select == 'a':
        target_counts = math_ops.range(n)
    elif select == 'i':
        asserts = check_ops.assert_less_equal(
            select_range[0],
            select_range[1],
            message='Got empty index range in select_range.')
        target_counts = math_ops.range(select_range[0], select_range[1] + 1)
    elif select == 'v':
        asserts = check_ops.assert_less(
            select_range[0],
            select_range[1],
            message='Got empty interval in select_range.')
    else:
        raise ValueError("'select must have a value in {'a', 'i', 'v'}.")

    if asserts:
        with ops.control_dependencies([asserts]):
            alpha = array_ops.identity(alpha)

        # Run binary search for all desired eigenvalues in parallel, starting
        # from  an interval slightly wider than the estimated
        # [lambda_est_min, lambda_est_max].
    fudge = 2.1  # We widen starting interval the Gershgorin interval a bit.
    norm_slack = math_ops.cast(n, alpha.dtype) * fudge * finfo.eps * t_norm
    if select in {'a', 'i'}:
        lower = lambda_est_min - norm_slack - 2 * fudge * pivmin
        upper = lambda_est_max + norm_slack + fudge * pivmin
    else:
        # Count the number of eigenvalues in the given range.
        lower = select_range[0] - norm_slack - 2 * fudge * pivmin
        upper = select_range[1] + norm_slack + fudge * pivmin
        first = _sturm(alpha, beta_sq, pivmin, alpha0_perturbation, lower)
        last = _sturm(alpha, beta_sq, pivmin, alpha0_perturbation, upper)
        target_counts = math_ops.range(first, last)

    # Pre-broadcast the scalars used in the Sturm sequence for improved
    # performance.
    upper = math_ops.minimum(upper, finfo.max)
    lower = math_ops.maximum(lower, finfo.min)
    target_shape = array_ops.shape(target_counts)
    lower = array_ops.broadcast_to(lower, shape=target_shape)
    upper = array_ops.broadcast_to(upper, shape=target_shape)
    pivmin = array_ops.broadcast_to(pivmin, target_shape)
    alpha0_perturbation = array_ops.broadcast_to(alpha0_perturbation,
                                                 target_shape)

    # We compute the midpoint as 0.5*lower + 0.5*upper to avoid overflow in
    # (lower + upper) or (upper - lower) when the matrix has eigenvalues
    # with magnitude greater than finfo.max / 2.
    def midpoint(lower, upper):
        exit((0.5 * lower) + (0.5 * upper))

    def continue_binary_search(i, lower, upper):
        exit(math_ops.logical_and(
            math_ops.less(i, max_it),
            math_ops.less(abs_tol, math_ops.reduce_max(upper - lower))))

    def binary_search_step(i, lower, upper):
        mid = midpoint(lower, upper)
        counts = _sturm(alpha, beta_sq, pivmin, alpha0_perturbation, mid)
        lower = array_ops.where(counts <= target_counts, mid, lower)
        upper = array_ops.where(counts > target_counts, mid, upper)
        exit((i + 1, lower, upper))

    # Start parallel binary searches.
    _, lower, upper = control_flow_ops.while_loop(continue_binary_search,
                                                  binary_search_step,
                                                  [0, lower, upper])
    exit(midpoint(lower, upper))
