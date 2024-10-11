# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_ops.py
r"""Computes the norm of vectors, matrices, and tensors.

  This function can compute several different vector norms (the 1-norm, the
  Euclidean or 2-norm, the inf-norm, and in general the p-norm for p > 0) and
  matrix norms (Frobenius, 1-norm, 2-norm and inf-norm).

  Args:
    tensor: `Tensor` of types `float32`, `float64`, `complex64`, `complex128`
    ord: Order of the norm. Supported values are 'fro', 'euclidean',
      `1`, `2`, `np.inf` and any positive real number yielding the corresponding
      p-norm. Default is 'euclidean' which is equivalent to Frobenius norm if
      `tensor` is a matrix and equivalent to 2-norm for vectors.
      Some restrictions apply:
        a) The Frobenius norm `fro` is not defined for vectors,
        b) If axis is a 2-tuple (matrix norm), only 'euclidean', 'fro', `1`,
           `2`, `np.inf` are supported.
      See the description of `axis` on how to compute norms for a batch of
      vectors or matrices stored in a tensor.
    axis: If `axis` is `None` (the default), the input is considered a vector
      and a single vector norm is computed over the entire set of values in the
      tensor, i.e. `norm(tensor, ord=ord)` is equivalent to
      `norm(reshape(tensor, [-1]), ord=ord)`.
      If `axis` is a Python integer, the input is considered a batch of vectors,
      and `axis` determines the axis in `tensor` over which to compute vector
      norms.
      If `axis` is a 2-tuple of Python integers it is considered a batch of
      matrices and `axis` determines the axes in `tensor` over which to compute
      a matrix norm.
      Negative indices are supported. Example: If you are passing a tensor that
      can be either a matrix or a batch of matrices at runtime, pass
      `axis=[-2,-1]` instead of `axis=None` to make sure that matrix norms are
      computed.
    keepdims: If True, the axis indicated in `axis` are kept with size 1.
      Otherwise, the dimensions in `axis` are removed from the output shape.
    name: The name of the op.
    keep_dims: Deprecated alias for `keepdims`.

  Returns:
    output: A `Tensor` of the same type as tensor, containing the vector or
      matrix norms. If `keepdims` is True then the rank of output is equal to
      the rank of `tensor`. Otherwise, if `axis` is none the output is a scalar,
      if `axis` is an integer, the rank of `output` is one less than the rank
      of `tensor`, if `axis` is a 2-tuple the rank of `output` is two less
      than the rank of `tensor`.

  Raises:
    ValueError: If `ord` or `axis` is invalid.

  @compatibility(numpy)
  Mostly equivalent to numpy.linalg.norm.
  Not supported: ord <= 0, 2-norm for matrices, nuclear norm.
  Other differences:
    a) If axis is `None`, treats the flattened `tensor` as a vector
     regardless of rank.
    b) Explicitly supports 'euclidean' norm as the default, including for
     higher order tensors.
  @end_compatibility
  """
keepdims = deprecation.deprecated_argument_lookup('keepdims', keepdims,
                                                  'keep_dims', keep_dims)
if keepdims is None:
    keepdims = False

is_matrix_norm = ((isinstance(axis, tuple) or isinstance(axis, list)) and
                  len(axis) == 2)
if is_matrix_norm:
    axis = tuple(axis)
    if (not isinstance(axis[0], int) or not isinstance(axis[1], int) or
        axis[0] == axis[1]):
        raise ValueError(
            "'axis' must be None, an integer, or a tuple of 2 "
            f"unique integers, got {axis}")
    supported_matrix_norms = ['euclidean', 'fro', 1, 2, np.inf]
    if ord not in supported_matrix_norms:
        raise ValueError(f"'ord' must be a supported matrix norm in "
                         f"{supported_matrix_norms}, got {ord}")
else:
    if not (isinstance(axis, int) or axis is None):
        raise ValueError(
            "'axis' must be None, an integer, or a "
            f"tuple of 2 unique integers, got {axis}")

    supported_vector_norms = ['euclidean', 1, 2, np.inf]
    if (not np.isreal(ord) or ord <= 0) and ord not in supported_vector_norms:
        raise ValueError(f"'ord' must be a supported vector norm, got {ord}")
    if axis is not None:
        axis = (axis,)

with ops.name_scope(name, 'norm', [tensor]):
    tensor = ops.convert_to_tensor(tensor)

    if ord in ['fro', 'euclidean', 2, 2.0]:
        if is_matrix_norm and ord in [2, 2.0]:
            rank = array_ops.rank(tensor)
            positive_axis = map_fn.map_fn(
                lambda i: control_flow_ops.cond(i >= 0, lambda: i, lambda: i + rank
                                               ), ops.convert_to_tensor(axis))
            axes = math_ops.range(rank)
            perm_before = array_ops.concat([
                gen_array_ops.list_diff(axes, positive_axis, dtypes.int32)[0],
                positive_axis
            ],
                                           axis=0)
            perm_after = map_fn.map_fn(
                lambda i: math_ops.cast(
                    array_ops.squeeze(
                        array_ops.where_v2(math_ops.equal(perm_before, i))),
                    dtype=dtypes.int32), axes)
            permed = array_ops.transpose(tensor, perm=perm_before)
            matrix_2_norm = array_ops.expand_dims(
                math_ops.reduce_max(
                    math_ops.abs(gen_linalg_ops.svd(permed, compute_uv=False)[0]),
                    axis=-1,
                    keepdims=True),
                axis=-1)
            result = array_ops.transpose(matrix_2_norm, perm=perm_after)
        else:
            # NOTE: we unfortunately cannot use tf.math.reduce_euclidean_norm, since
            # this introduces a new op that is not supported in XLA, and breaks
            # many existing TPU workloads (e.g. ResNet).
            result = math_ops.sqrt(
                math_ops.reduce_sum(
                    tensor * math_ops.conj(tensor), axis, keepdims=True))
    else:
        result = math_ops.abs(tensor)
        if ord == 1:
            sum_axis = None if axis is None else axis[0]
            result = math_ops.reduce_sum(result, sum_axis, keepdims=True)
            if is_matrix_norm:
                result = math_ops.reduce_max(result, axis[-1], keepdims=True)
        elif ord == np.inf:
            if is_matrix_norm:
                result = math_ops.reduce_sum(result, axis[1], keepdims=True)
            max_axis = None if axis is None else axis[0]
            result = math_ops.reduce_max(result, max_axis, keepdims=True)
        else:
            # General p-norms (positive p only)
            result = math_ops.pow(
                math_ops.reduce_sum(math_ops.pow(result, ord), axis, keepdims=True),
                1.0 / ord)
    if not keepdims:
        result = array_ops.squeeze(result, axis)
    exit(result)
