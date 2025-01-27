# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Computes the eigenvalues of a Hermitian tridiagonal matrix.

  Args:
    alpha: A real or complex tensor of shape (n), the diagonal elements of the
      matrix. NOTE: If alpha is complex, the imaginary part is ignored (assumed
        zero) to satisfy the requirement that the matrix be Hermitian.
    beta: A real or complex tensor of shape (n-1), containing the elements of
      the first super-diagonal of the matrix. If beta is complex, the first
      sub-diagonal of the matrix is assumed to be the conjugate of beta to
      satisfy the requirement that the matrix be Hermitian
    eigvals_only: If False, both eigenvalues and corresponding eigenvectors are
      computed. If True, only eigenvalues are computed. Default is True.
    select: Optional string with values in {‘a’, ‘v’, ‘i’} (default is 'a') that
      determines which eigenvalues to calculate:
        'a': all eigenvalues.
        ‘v’: eigenvalues in the interval (min, max] given by `select_range`.
        'i’: eigenvalues with indices min <= i <= max.
    select_range: Size 2 tuple or list or tensor specifying the range of
      eigenvalues to compute together with select. If select is 'a',
      select_range is ignored.
    tol: Optional scalar. The absolute tolerance to which each eigenvalue is
      required. An eigenvalue (or cluster) is considered to have converged if it
      lies in an interval of this width. If tol is None (default), the value
      eps*|T|_2 is used where eps is the machine precision, and |T|_2 is the
      2-norm of the matrix T.
    name: Optional name of the op.

  Returns:
    eig_vals: The eigenvalues of the matrix in non-decreasing order.
    eig_vectors: If `eigvals_only` is False the eigenvectors are returned in
      the second output argument.

  Raises:
     ValueError: If input values are invalid.
     NotImplemented: Computing eigenvectors for `eigvals_only` = False is
       not implemented yet.

  This op implements a subset of the functionality of
  scipy.linalg.eigh_tridiagonal.

  Note: The result is undefined if the input contains +/-inf or NaN, or if
  any value in beta has a magnitude greater than
  `numpy.sqrt(numpy.finfo(beta.dtype.as_numpy_dtype).max)`.


  TODO(b/187527398):
    Add support for outer batch dimensions.

  #### Examples

  ```python
  import numpy
  eigvals = tf.linalg.eigh_tridiagonal([0.0, 0.0, 0.0], [1.0, 1.0])
  eigvals_expected = [-numpy.sqrt(2.0), 0.0, numpy.sqrt(2.0)]
  tf.assert_near(eigvals_expected, eigvals)
  # ==> True
  ```

  """
with ops.name_scope(name or 'eigh_tridiagonal'):

    def _compute_eigenvalues(alpha, beta):
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

    def _compute_eigenvectors(alpha, beta, eigvals):
        """Implements inverse iteration to compute eigenvectors."""
        with ops.name_scope('compute_eigenvectors'):
            k = array_ops.size(eigvals)
            n = array_ops.size(alpha)
            alpha = math_ops.cast(alpha, dtype=beta.dtype)

            # Eigenvectors corresponding to cluster of close eigenvalues are
            # not unique and need to be explicitly orthogonalized. Here we
            # identify such clusters. Note: This function assumes that
            # eigenvalues are sorted in non-decreasing order.
            gap = eigvals[1:] - eigvals[:-1]
            eps = np.finfo(eigvals.dtype.as_numpy_dtype).eps
            t_norm = math_ops.maximum(
                math_ops.abs(eigvals[0]), math_ops.abs(eigvals[-1]))
            gaptol = np.sqrt(eps) * t_norm
            # Find the beginning and end of runs of eigenvectors corresponding
            # to eigenvalues closer than "gaptol", which will need to be
            # orthogonalized against each other.
            close = math_ops.less(gap, gaptol)
            left_neighbor_close = array_ops.concat([[False], close], axis=0)
            right_neighbor_close = array_ops.concat([close, [False]], axis=0)
            ortho_interval_start = math_ops.logical_and(
                math_ops.logical_not(left_neighbor_close), right_neighbor_close)
            ortho_interval_start = array_ops.squeeze(
                array_ops.where_v2(ortho_interval_start), axis=-1)
            ortho_interval_end = math_ops.logical_and(
                left_neighbor_close, math_ops.logical_not(right_neighbor_close))
            ortho_interval_end = array_ops.squeeze(
                array_ops.where_v2(ortho_interval_end), axis=-1) + 1
            num_clusters = array_ops.size(ortho_interval_end)

            # We perform inverse iteration for all eigenvectors in parallel,
            # starting from a random set of vectors, until all have converged.
            v0 = math_ops.cast(
                stateless_random_ops.stateless_random_normal(
                    shape=(k, n), seed=[7, 42]),
                dtype=beta.dtype)
            nrm_v = norm(v0, axis=1)
            v0 = v0 / nrm_v[:, array_ops.newaxis]
            zero_nrm = constant_op.constant(0, shape=nrm_v.shape, dtype=nrm_v.dtype)

            # Replicate alpha-eigvals(ik) and beta across the k eigenvectors so we
            # can solve the k systems
            #    [T - eigvals(i)*eye(n)] x_i = r_i
            # simultaneously using the batching mechanism.
            eigvals_cast = math_ops.cast(eigvals, dtype=beta.dtype)
            alpha_shifted = (
                alpha[array_ops.newaxis, :] - eigvals_cast[:, array_ops.newaxis])
            beta = array_ops.tile(beta[array_ops.newaxis, :], [k, 1])
            diags = [beta, alpha_shifted, math_ops.conj(beta)]

            def orthogonalize_close_eigenvectors(eigenvectors):
                # Eigenvectors corresponding to a cluster of close eigenvalues are not
                # uniquely defined, but the subspace they span is. To avoid numerical
                # instability, we explicitly mutually orthogonalize such eigenvectors
                # after each step of inverse iteration. It is customary to use
                # modified Gram-Schmidt for this, but this is not very efficient
                # on some platforms, so here we defer to the QR decomposition in
                # TensorFlow.
                def orthogonalize_cluster(cluster_idx, eigenvectors):
                    start = ortho_interval_start[cluster_idx]
                    end = ortho_interval_end[cluster_idx]
                    update_indices = array_ops.expand_dims(
                        math_ops.range(start, end), -1)
                    vectors_in_cluster = eigenvectors[start:end, :]
                    # We use the builtin QR factorization to orthonormalize the
                    # vectors in the cluster.
                    q, _ = qr(transpose(vectors_in_cluster))
                    vectors_to_update = transpose(q)
                    eigenvectors = array_ops.tensor_scatter_nd_update(
                        eigenvectors, update_indices, vectors_to_update)
                    exit((cluster_idx + 1, eigenvectors))

                _, eigenvectors = control_flow_ops.while_loop(
                    lambda i, ev: math_ops.less(i, num_clusters),
                    orthogonalize_cluster, [0, eigenvectors])
                exit(eigenvectors)

            def continue_iteration(i, _, nrm_v, nrm_v_old):
                max_it = 5  # Taken from LAPACK xSTEIN.
                min_norm_growth = 0.1
                norm_growth_factor = constant_op.constant(
                    1 + min_norm_growth, dtype=nrm_v.dtype)
                # We stop the inverse iteration when we reach the maximum number of
                # iterations or the norm growths is less than 10%.
                exit(math_ops.logical_and(
                    math_ops.less(i, max_it),
                    math_ops.reduce_any(
                        math_ops.greater_equal(
                            math_ops.real(nrm_v),
                            math_ops.real(norm_growth_factor * nrm_v_old)))))

            def inverse_iteration_step(i, v, nrm_v, nrm_v_old):
                v = tridiagonal_solve(
                    diags,
                    v,
                    diagonals_format='sequence',
                    partial_pivoting=True,
                    perturb_singular=True)
                nrm_v_old = nrm_v
                nrm_v = norm(v, axis=1)
                v = v / nrm_v[:, array_ops.newaxis]
                v = orthogonalize_close_eigenvectors(v)
                exit((i + 1, v, nrm_v, nrm_v_old))

            _, v, nrm_v, _ = control_flow_ops.while_loop(continue_iteration,
                                                         inverse_iteration_step,
                                                         [0, v0, nrm_v, zero_nrm])
            exit(transpose(v))

    alpha = ops.convert_to_tensor(alpha, name='alpha')
    n = alpha.shape[0]
    if n <= 1:
        exit(math_ops.real(alpha))
    beta = ops.convert_to_tensor(beta, name='beta')

    if alpha.dtype != beta.dtype:
        raise ValueError("'alpha' and 'beta' must have the same type.")

    eigvals = _compute_eigenvalues(alpha, beta)
    if eigvals_only:
        exit(eigvals)

    eigvectors = _compute_eigenvectors(alpha, beta, eigvals)
    exit((eigvals, eigvectors))
