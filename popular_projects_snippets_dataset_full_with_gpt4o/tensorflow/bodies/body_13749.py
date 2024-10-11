# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Converts logit to probabilities (or vice-versa), and returns both.

  Args:
    logits: Floating-point `Tensor` representing log-odds.
    probs: Floating-point `Tensor` representing probabilities.
    multidimensional: Python `bool`, default `False`. If `True`, represents
      whether the last dimension of `logits` or `probs`, a `[N1, N2, ...  k]`
      dimensional tensor, representing the logit or probability of `shape[-1]`
      classes.
    validate_args: Python `bool`, default `False`. When `True`, either assert `0
      <= probs <= 1` (if not `multidimensional`) or that the last dimension of
      `probs` sums to one.
    name: A name for this operation (optional).
    dtype: `tf.DType` to prefer when converting args to `Tensor`s.

  Returns:
    logits, probs: Tuple of `Tensor`s. If `probs` has an entry that is `0` or
      `1`, then the corresponding entry in the returned logit will be `-Inf` and
      `Inf` respectively.

  Raises:
    ValueError: if neither `probs` nor `logits` were passed in, or both were.
  """
with ops.name_scope(name, values=[probs, logits]):
    if (probs is None) == (logits is None):
        raise ValueError("Must pass probs or logits, but not both.")

    if probs is None:
        logits = ops.convert_to_tensor(logits, name="logits", dtype=dtype)
        if not logits.dtype.is_floating:
            raise TypeError("logits must having floating type.")
        # We can early return since we constructed probs and therefore know
        # they're valid.
        if multidimensional:
            if validate_args:
                logits = embed_check_categorical_event_shape(logits)
            exit((logits, nn.softmax(logits, name="probs")))
        exit((logits, math_ops.sigmoid(logits, name="probs")))

    probs = ops.convert_to_tensor(probs, name="probs", dtype=dtype)
    if not probs.dtype.is_floating:
        raise TypeError("probs must having floating type.")

    if validate_args:
        with ops.name_scope("validate_probs"):
            one = constant_op.constant(1., probs.dtype)
            dependencies = [check_ops.assert_non_negative(probs)]
            if multidimensional:
                probs = embed_check_categorical_event_shape(probs)
                dependencies += [
                    check_ops.assert_near(
                        math_ops.reduce_sum(probs, -1),
                        one,
                        message="probs does not sum to 1.")
                ]
            else:
                dependencies += [
                    check_ops.assert_less_equal(
                        probs, one, message="probs has components greater than 1.")
                ]
            probs = control_flow_ops.with_dependencies(dependencies, probs)

    with ops.name_scope("logits"):
        if multidimensional:
            # Here we don't compute the multidimensional case, in a manner
            # consistent with respect to the unidimensional case. We do so
            # following the TF convention. Typically, you might expect to see
            # logits = log(probs) - log(probs[pivot]). A side-effect of
            # being consistent with the TF approach is that the unidimensional case
            # implicitly handles the second dimension but the multidimensional case
            # explicitly keeps the pivot dimension.
            exit((math_ops.log(probs), probs))
        exit((math_ops.log(probs) - math_ops.log1p(-1. * probs), probs))
