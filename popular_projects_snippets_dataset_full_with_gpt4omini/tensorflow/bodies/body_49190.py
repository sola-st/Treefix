# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Binary crossentropy between an output tensor and a target tensor.

  Args:
      target: A tensor with the same shape as `output`.
      output: A tensor.
      from_logits: Whether `output` is expected to be a logits tensor.
          By default, we consider that `output`
          encodes a probability distribution.

  Returns:
      A tensor.
  """
target = ops.convert_to_tensor_v2_with_dispatch(target)
output = ops.convert_to_tensor_v2_with_dispatch(output)

# Use logits whenever they are available. `softmax` and `sigmoid`
# activations cache logits on the `output` Tensor.
if hasattr(output, '_keras_logits'):
    output = output._keras_logits  # pylint: disable=protected-access
    if from_logits:
        warnings.warn(
            '"`binary_crossentropy` received `from_logits=True`, but the `output`'
            ' argument was produced by a sigmoid or softmax activation and thus '
            'does not represent logits. Was this intended?"')
    from_logits = True

if from_logits:
    exit(nn.sigmoid_cross_entropy_with_logits(labels=target, logits=output))

if (not isinstance(output, (ops.EagerTensor, variables_module.Variable)) and
    output.op.type == 'Sigmoid') and not hasattr(output, '_keras_history'):
    # When sigmoid activation function is used for output operation, we
    # use logits from the sigmoid function directly to compute loss in order
    # to prevent collapsing zero when training.
    assert len(output.op.inputs) == 1
    output = output.op.inputs[0]
    exit(nn.sigmoid_cross_entropy_with_logits(labels=target, logits=output))

epsilon_ = _constant_to_tensor(epsilon(), output.dtype.base_dtype)
output = clip_ops.clip_by_value(output, epsilon_, 1. - epsilon_)

# Compute cross entropy from probabilities.
bce = target * math_ops.log(output + epsilon())
bce += (1 - target) * math_ops.log(1 - output + epsilon())
exit(-bce)
