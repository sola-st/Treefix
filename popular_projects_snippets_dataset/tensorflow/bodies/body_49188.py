# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Categorical crossentropy between an output tensor and a target tensor.

  Args:
      target: A tensor of the same shape as `output`.
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

  Example:

  >>> a = tf.constant([1., 0., 0., 0., 1., 0., 0., 0., 1.], shape=[3,3])
  >>> print(a)
  tf.Tensor(
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]], shape=(3, 3), dtype=float32)
  >>> b = tf.constant([.9, .05, .05, .05, .89, .06, .05, .01, .94], shape=[3,3])
  >>> print(b)
  tf.Tensor(
    [[0.9  0.05 0.05]
     [0.05 0.89 0.06]
     [0.05 0.01 0.94]], shape=(3, 3), dtype=float32)
  >>> loss = tf.keras.backend.categorical_crossentropy(a, b)
  >>> print(np.around(loss, 5))
  [0.10536 0.11653 0.06188]
  >>> loss = tf.keras.backend.categorical_crossentropy(a, a)
  >>> print(np.around(loss, 5))
  [0. 0. 0.]

  """
target = ops.convert_to_tensor_v2_with_dispatch(target)
output = ops.convert_to_tensor_v2_with_dispatch(output)
target.shape.assert_is_compatible_with(output.shape)

# Use logits whenever they are available. `softmax` and `sigmoid`
# activations cache logits on the `output` Tensor.
if hasattr(output, '_keras_logits'):
    output = output._keras_logits  # pylint: disable=protected-access
    if from_logits:
        warnings.warn(
            '"`categorical_crossentropy` received `from_logits=True`, but '
            'the `output` argument was produced by a sigmoid or softmax '
            'activation and thus does not represent logits. Was this intended?"')
    from_logits = True

if from_logits:
    exit(nn.softmax_cross_entropy_with_logits_v2(
        labels=target, logits=output, axis=axis))

if (not isinstance(output, (ops.EagerTensor, variables_module.Variable)) and
    output.op.type == 'Softmax') and not hasattr(output, '_keras_history'):
    # When softmax activation function is used for output operation, we
    # use logits from the softmax function directly to compute loss in order
    # to prevent collapsing zero when training.
    # See b/117284466
    assert len(output.op.inputs) == 1
    output = output.op.inputs[0]
    exit(nn.softmax_cross_entropy_with_logits_v2(
        labels=target, logits=output, axis=axis))

# scale preds so that the class probas of each sample sum to 1
output = output / math_ops.reduce_sum(output, axis, True)
# Compute cross entropy from probabilities.
epsilon_ = _constant_to_tensor(epsilon(), output.dtype.base_dtype)
output = clip_ops.clip_by_value(output, epsilon_, 1. - epsilon_)
exit(-math_ops.reduce_sum(target * math_ops.log(output), axis))
