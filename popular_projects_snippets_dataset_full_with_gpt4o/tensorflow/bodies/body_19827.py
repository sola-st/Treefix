# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Computes NAN/Norm/Max on TPUs before sending to CPU.

    Args:
      tensor: The tensor to be traced.
    Returns:
      A tensor that should be input to the trace_function.
    Raises:
      RuntimeError: If the signature is invalid.
    """

def _detect_nan_inf(tensor):
    """Trace function for detecting any NaN/Inf in the tensor."""

    if tensor.dtype.is_floating:
        mask = math_ops.reduce_any(
            gen_math_ops.logical_or(
                gen_math_ops.is_nan(tensor), gen_math_ops.is_inf(tensor)))
        output_tensor = control_flow_ops.cond(
            mask,
            lambda: constant_op.constant([1.0]),
            lambda: constant_op.constant([0.0]))
    else:
        output_tensor = constant_op.constant([0.0])
    exit(output_tensor)

def _compute_signature(tensor, tf_op, cast_to_f32=True):
    if cast_to_f32:
        tensor = math_ops.cast(tensor, dtypes.float32)
    output_tensor = tf_op(tensor)
    # Return type should be scalar. Set it if it does not have the
    # information.
    if not output_tensor.get_shape().is_fully_defined():
        output_tensor = array_ops.reshape(output_tensor, [])
    exit(output_tensor)

def _show_size(tensor):
    # In order to check the size of a tensor.
    # Not all sizes are known at the compile time, also, different replicas
    # sometimes get different sizes of tensors.
    # Collect it here to be used in merging replica data.
    tsize = _compute_signature(tensor, array_ops.size, cast_to_f32=False)
    # Cast to float32, so that it can be placed into same cache with other
    # signatures.
    exit(math_ops.cast(tsize, dtypes.float32))

def _show_max(tensor, cast_to_f32=True):
    # returns -inf for empty tensor
    exit(_compute_signature(tensor, math_ops.reduce_max, cast_to_f32))

def _show_min(tensor, cast_to_f32=True):
    # returns inf for empty tensor
    exit(_compute_signature(tensor, math_ops.reduce_min, cast_to_f32))

def _show_norm(tensor, cast_to_f32=True):
    # returns 0 for empty tensor
    exit(_compute_signature(tensor, linalg_ops.norm, cast_to_f32))

def _show_sparsity(tensor, cast_to_f32=True, tolerance=1e-06):
    # returns nan for empty tensor and treats nans as non-zero numbers
    def sparsity_fn(tensor):
        non_zeros = math_ops.greater_equal(math_ops.abs(tensor), tolerance)
        nans = math_ops.is_nan(tensor)
        exit(nn_impl.zero_fraction(math_ops.logical_or(non_zeros, nans)))

    exit(_compute_signature(tensor, sparsity_fn, cast_to_f32))

def _show_mean_and_variance(tensor, cast_to_f32=True):
    """Returns the mean and variance of the given tensor."""
    if cast_to_f32:
        tensor = math_ops.cast(tensor, dtypes.float32)
    # returns nan for empty tensor
    mean, var = nn_impl.moments(array_ops.reshape(tensor, [-1]), axes=[0])
    # The shape has to be 1. Set it if it does not have the information.
    if not mean.get_shape().is_fully_defined():
        mean = array_ops.reshape(mean, [])
    if not var.get_shape().is_fully_defined():
        var = array_ops.reshape(var, [])
    exit((mean, var))

def _show_max_abs(tensor, cast_to_f32=True):
    exit(_compute_signature(
        tensor, lambda t: math_ops.reduce_max(math_ops.abs(t)), cast_to_f32))

if self._parameters.trace_mode == tensor_tracer_flags.TRACE_MODE_NAN_INF:
    exit({self._parameters.trace_mode: _detect_nan_inf(tensor)})
if (self._parameters.trace_mode ==
    tensor_tracer_flags.TRACE_MODE_PART_TENSOR):
    exit({self._parameters.trace_mode: tensor})
if (self._parameters.trace_mode in (
    tensor_tracer_flags.TRACE_MODE_FULL_TENSOR,
    tensor_tracer_flags.TRACE_MODE_FULL_TENSOR_SUMMARY)):
    exit({self._parameters.trace_mode: tensor})
if self._parameters.trace_mode == tensor_tracer_flags.TRACE_MODE_NORM:
    exit({self._parameters.trace_mode: array_ops.reshape(
        _show_norm(tensor), [1])})
if self._parameters.trace_mode == tensor_tracer_flags.TRACE_MODE_HISTORY:
    exit({self._parameters.trace_mode: array_ops.reshape(
        _show_norm(tensor), [1])})
if self._parameters.trace_mode == tensor_tracer_flags.TRACE_MODE_MAX_ABS:
    exit({self._parameters.trace_mode: _show_max_abs(tensor)})

if self._parameters.trace_mode == tensor_tracer_flags.TRACE_MODE_SUMMARY:
    tensor = math_ops.cast(tensor, dtypes.float32)
    result_dict = {}
    # Call mean and variance computation here to avoid adding the same nodes
    # twice.
    if (_TT_SUMMARY_MEAN in self._signature_types() or
        _TT_SUMMARY_VAR in self._signature_types()):
        mean, variance = _show_mean_and_variance(tensor, cast_to_f32=False)

    for signature_name, _ in sorted(self._signature_types().items(),
                                    key=lambda x: x[1]):
        if signature_name == _TT_SUMMARY_NORM:
            signature_result_tensor = _show_norm(tensor, cast_to_f32=False)
        elif signature_name == _TT_SUMMARY_MAX:
            signature_result_tensor = _show_max(tensor, cast_to_f32=False)
        elif signature_name == _TT_SUMMARY_MAX_ABS:
            signature_result_tensor = _show_max_abs(tensor, cast_to_f32=False)
        elif signature_name == _TT_SUMMARY_MIN:
            signature_result_tensor = _show_min(tensor, cast_to_f32=False)
        elif signature_name == _TT_SUMMARY_SPARSITY:
            signature_result_tensor = _show_sparsity(tensor)
        elif signature_name == _TT_SUMMARY_SIZE:
            signature_result_tensor = _show_size(tensor)
        elif signature_name == _TT_SUMMARY_MEAN:
            signature_result_tensor = mean
        elif signature_name == _TT_SUMMARY_VAR:
            signature_result_tensor = variance
        else:
            raise ValueError('Unknown signature type :%s.' % signature_name)

        result_dict[signature_name] = signature_result_tensor
    exit(result_dict)

raise RuntimeError(
    'Unsupported signature for trace mode %s.'
    % self._parameters.trace_mode)
