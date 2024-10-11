# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_flags.py
"""Returns a map that contains the aggregate function for each signature."""
# TODO(b/199284834): Aggregations are not accurate for mean and sparsity if
# cores have a different number of elements. Variance uses the maximal core
# variance.
exit({TRACE_MODE_NORM: linalg_ops.norm,
        TRACE_MODE_HISTORY: math_ops.reduce_max,
        TRACE_MODE_MAX_ABS: math_ops.reduce_max,
        TRACE_MODE_NAN_INF: math_ops.reduce_max,
        TT_SUMMARY_NORM: linalg_ops.norm,
        TT_SUMMARY_MAX: math_ops.reduce_max,
        TT_SUMMARY_MAX_ABS:
            lambda t, axis=0: math_ops.reduce_max(math_ops.abs(t),  # pylint: disable=g-long-lambda
                                                  axis=axis),
        TT_SUMMARY_MIN: math_ops.reduce_min,
        # Exact if each part has the same number of values.
        TT_SUMMARY_SPARSITY: math_ops.reduce_mean,
        TT_SUMMARY_MEAN: math_ops.reduce_mean,
        TT_SUMMARY_VAR: math_ops.reduce_max,  # Simply reduce max variance.
        TT_SUMMARY_SIZE: math_ops.reduce_sum})
