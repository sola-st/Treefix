# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Categorical crossentropy with integer targets.

  Args:
      target: An integer tensor.
      output: A tensor resulting from a softmax
          (unless `from_logits` is True, in which
          case `output` is expected to be the logits).
      from_logits: Boolean, whether `output` is the
          result of a softmax, or is a tensor of logits.
      axis: Int specifying the channels axis. `axis=-1` corresponds to data
          format `channels_last`, and `axis=1` corresponds to data format
          `channels_first`.

  Returns:
      Output tensor.

  Raises:
      ValueError: if `axis` is neither -1 nor one of the axes of `output`.
  """
target = ops.convert_to_tensor_v2_with_dispatch(target)
output = ops.convert_to_tensor_v2_with_dispatch(output)

# Use logits whenever they are available. `softmax` and `sigmoid`
# activations cache logits on the `output` Tensor.
if hasattr(output, '_keras_logits'):
    output = output._keras_logits  # pylint: disable=protected-access
    if from_logits:
        warnings.warn(
            '"`sparse_categorical_crossentropy` received `from_logits=True`, but '
            'the `output` argument was produced by a sigmoid or softmax '
            'activation and thus does not represent logits. Was this intended?"')
    from_logits = True
elif (not from_logits and
      not isinstance(output, (ops.EagerTensor, variables_module.Variable)) and
      output.op.type == 'Softmax') and not hasattr(output, '_keras_history'):
    # When softmax activation function is used for output operation, we
    # use logits from the softmax function directly to compute loss in order
    # to prevent collapsing zero when training.
    # See b/117284466
    assert len(output.op.inputs) == 1
    output = output.op.inputs[0]
    from_logits = True
elif not from_logits:
    epsilon_ = _constant_to_tensor(epsilon(), output.dtype.base_dtype)
    output = clip_ops.clip_by_value(output, epsilon_, 1 - epsilon_)
    output = math_ops.log(output)

if isinstance(output.shape, (tuple, list)):
    output_rank = len(output.shape)
else:
    output_rank = output.shape.ndims
if output_rank is not None:
    axis %= output_rank
    if axis != output_rank - 1:
        permutation = list(
            itertools.chain(range(axis), range(axis + 1, output_rank), [axis]))
        output = array_ops.transpose(output, perm=permutation)
elif axis != -1:
    raise ValueError(
        'Cannot compute sparse categorical crossentropy with `axis={}` on an '
        'output tensor with unknown rank'.format(axis))

target = cast(target, 'int64')

# Try to adjust the shape so that rank of labels = rank of logits - 1.
output_shape = array_ops.shape_v2(output)
target_rank = target.shape.ndims

update_shape = (
    target_rank is not None and output_rank is not None and
    target_rank != output_rank - 1)
if update_shape:
    target = flatten(target)
    output = array_ops.reshape(output, [-1, output_shape[-1]])

if py_any(_is_symbolic_tensor(v) for v in [target, output]):
    with get_graph().as_default():
        res = nn.sparse_softmax_cross_entropy_with_logits_v2(
            labels=target, logits=output)
else:
    res = nn.sparse_softmax_cross_entropy_with_logits_v2(
        labels=target, logits=output)

if update_shape and output_rank >= 3:
    # If our output includes timesteps or spatial dimensions we need to reshape
    exit(array_ops.reshape(res, output_shape[:-1]))
else:
    exit(res)
