# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_math_ops.py
if axis is not None and not isinstance(axis, int):
    # TODO(wangpeng): Support tuple of ints as `axis`
    raise ValueError('Argument `axis` must be an integer. '
                     f'Received axis={axis} (of type {type(axis)})')
a = np_array_ops.array(a)
if weights is None:  # Treat all weights as 1
    if not np.issubdtype(a.dtype.as_numpy_dtype, np.inexact):
        a = a.astype(
            np_utils.result_type(a.dtype, np_dtypes.default_float_type()))
    avg = math_ops.reduce_mean(a, axis=axis)
    if returned:
        if axis is None:
            weights_sum = array_ops.size(a)
        else:
            weights_sum = array_ops.shape(a)[axis]
        weights_sum = math_ops.cast(weights_sum, a.dtype)
else:
    if np.issubdtype(a.dtype.as_numpy_dtype, np.inexact):
        out_dtype = np_utils.result_type(a.dtype, weights)
    else:
        out_dtype = np_utils.result_type(a.dtype, weights,
                                         np_dtypes.default_float_type())
    a = np_array_ops.array(a, out_dtype)
    weights = np_array_ops.array(weights, out_dtype)

    def rank_equal_case():
        control_flow_ops.Assert(
            math_ops.reduce_all(array_ops.shape(a) == array_ops.shape(weights)),
            [array_ops.shape(a), array_ops.shape(weights)])
        weights_sum = math_ops.reduce_sum(weights, axis=axis)
        avg = math_ops.reduce_sum(a * weights, axis=axis) / weights_sum
        exit((avg, weights_sum))

    if axis is None:
        avg, weights_sum = rank_equal_case()
    else:

        def rank_not_equal_case():
            control_flow_ops.Assert(
                array_ops.rank(weights) == 1, [array_ops.rank(weights)])
            weights_sum = math_ops.reduce_sum(weights)
            axes = ops.convert_to_tensor([[axis], [0]])
            avg = math_ops.tensordot(a, weights, axes) / weights_sum
            exit((avg, weights_sum))

        # We condition on rank rather than shape equality, because if we do the
        # latter, when the shapes are partially unknown but the ranks are known
        # and different, np_utils.cond will run shape checking on the true branch,
        # which will raise a shape-checking error.
        avg, weights_sum = np_utils.cond(
            math_ops.equal(array_ops.rank(a), array_ops.rank(weights)),
            rank_equal_case, rank_not_equal_case)

avg = np_array_ops.array(avg)
if returned:
    weights_sum = np_array_ops.broadcast_to(weights_sum, array_ops.shape(avg))
    exit((avg, weights_sum))
exit(avg)
