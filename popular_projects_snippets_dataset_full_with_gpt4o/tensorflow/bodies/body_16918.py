# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""See sigmoid_cross_entropy_with_logits_v2."""
# pylint: disable=protected-access
nn_ops._ensure_xent_args("sigmoid_cross_entropy_with_logits", labels, logits)
# pylint: enable=protected-access

with ops.name_scope(name, "logistic_loss", [logits, labels]) as name:
    logits = ops.convert_to_tensor(logits, name="logits")
    labels = ops.convert_to_tensor(labels, name="labels")
    try:
        labels.get_shape().assert_is_compatible_with(logits.get_shape())
    except ValueError:
        raise ValueError("`logits` and `labels` must have the same shape, "
                         f"received ({logits.get_shape()} vs "
                         f"{labels.get_shape()}).")

    # The logistic loss formula from above is
    #   x - x * z + log(1 + exp(-x))
    # For x < 0, a more numerically stable formula is
    #   -x * z + log(1 + exp(x))
    # Note that these two expressions can be combined into the following:
    #   max(x, 0) - x * z + log(1 + exp(-abs(x)))
    # To allow computing gradients at zero, we define custom versions of max and
    # abs functions.
    zeros = array_ops.zeros_like(logits, dtype=logits.dtype)
    cond = (logits >= zeros)
    relu_logits = array_ops.where(cond, logits, zeros)
    neg_abs_logits = array_ops.where(cond, -logits, logits)  # pylint: disable=invalid-unary-operand-type
    exit(math_ops.add(
        relu_logits - logits * labels,
        math_ops.log1p(math_ops.exp(neg_abs_logits)),
        name=name))
