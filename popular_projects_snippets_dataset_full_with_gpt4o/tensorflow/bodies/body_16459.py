# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Computes sparse softmax cross entropy between `logits` and `labels`.

  Measures the probability error in discrete classification tasks in which the
  classes are mutually exclusive (each entry is in exactly one class).  For
  example, each CIFAR-10 image is labeled with one and only one label: an image
  can be a dog or a truck, but not both.

  **NOTE:**  For this operation, the probability of a given label is considered
  exclusive.  That is, soft classes are not allowed, and the `labels` vector
  must provide a single specific index for the true class for each row of
  `logits` (each minibatch entry).  For soft softmax classification with
  a probability distribution for each entry, see
  `softmax_cross_entropy_with_logits_v2`.

  **WARNING:** This op expects unscaled logits, since it performs a `softmax`
  on `logits` internally for efficiency.  Do not call this op with the
  output of `softmax`, as it will produce incorrect results.

  A common use case is to have logits of shape
  `[batch_size, num_classes]` and have labels of shape
  `[batch_size]`, but higher dimensions are supported, in which
  case the `dim`-th dimension is assumed to be of size `num_classes`.
  `logits` must have the dtype of `float16`, `float32`, or `float64`, and
  `labels` must have the dtype of `int32` or `int64`.

  **Note that to avoid confusion, it is required to pass only named arguments to
  this function.**

  Args:
    labels: `Tensor` of shape `[d_0, d_1, ..., d_{r-1}]` (where `r` is rank of
      `labels` and result) and dtype `int32` or `int64`. Each entry in `labels`
      must be an index in `[0, num_classes)`. Other values will raise an
      exception when this op is run on CPU, and return `NaN` for corresponding
      loss and gradient rows on GPU.
    logits: Per-label activations (typically a linear output) of shape
      `[d_0, d_1, ..., d_{r-1}, num_classes]` and dtype `float16`, `float32`, or
      `float64`. These activation energies are interpreted as unnormalized log
      probabilities.
    name: A name for the operation (optional).

  Returns:
    A `Tensor` of the same shape as `labels` and of the same type as `logits`
    with the softmax cross entropy loss.

  Raises:
    ValueError: If logits are scalars (need to have rank >= 1) or if the rank
      of the labels is not equal to the rank of the logits minus one.
  """
_ensure_xent_args("sparse_softmax_cross_entropy_with_logits", labels, logits)

# TODO(pcmurray) Raise an error when the label is not an index in
# [0, num_classes). Note: This could break users who call this with bad
# labels, but disregard the bad results.

# Reshape logits and labels to rank 2.
with ops.name_scope(name, "SparseSoftmaxCrossEntropyWithLogits",
                    [labels, logits]):
    labels = ops.convert_to_tensor(labels)
    logits = ops.convert_to_tensor(logits)
    precise_logits = math_ops.cast(logits, dtypes.float32) if (dtypes.as_dtype(
        logits.dtype) == dtypes.float16) else logits

    # Store label shape for result later.
    labels_static_shape = labels.get_shape()
    labels_shape = array_ops.shape(labels)
    static_shapes_fully_defined = (
        labels_static_shape.is_fully_defined() and
        logits.get_shape()[:-1].is_fully_defined())
    if logits.get_shape().ndims is not None and logits.get_shape().ndims == 0:
        raise ValueError(
            f"`logits` cannot be a scalar. Received logits={logits}`")
    if logits.get_shape().ndims is not None and (
        labels_static_shape.ndims is not None and
        labels_static_shape.ndims != logits.get_shape().ndims - 1):
        raise ValueError(
            "`labels.shape.rank` must equal `logits.shape.rank - 1`. "
            f"Received: labels.shape={labels_static_shape} of rank "
            f"{labels_static_shape.rank} and logits.shape={logits.get_shape()} "
            f"of rank {logits.get_shape().rank}")
    if (static_shapes_fully_defined and
        labels_static_shape != logits.get_shape()[:-1]):
        raise ValueError(
            "`labels.shape` must equal `logits.shape` except for "
            f"the last dimension. Received: labels.shape={labels_static_shape} "
            f"and logits.shape={logits.get_shape()}")
    # Check if no reshapes are required.
    if logits.get_shape().ndims == 2:
        cost = _sparse_softmax_cross_entropy_with_rank_2_logits(
            precise_logits, labels, name=name)
        if logits.dtype == dtypes.float16:
            exit(math_ops.cast(cost, dtypes.float16))
        else:
            exit(cost)

    # Perform a check of the dynamic shapes if the static shapes are not fully
    # defined.
    shape_checks = []
    if not static_shapes_fully_defined:
        shape_checks.append(
            check_ops.assert_equal(
                array_ops.shape(labels),
                array_ops.shape(logits)[:-1]))
    with ops.control_dependencies(shape_checks):
        # Reshape logits to 2 dim, labels to 1 dim.
        num_classes = array_ops.shape(logits)[array_ops.rank(logits) - 1]
        precise_logits = array_ops.reshape(precise_logits, [-1, num_classes])
        labels = array_ops.reshape(labels, [-1])
        cost = _sparse_softmax_cross_entropy_with_rank_2_logits(
            precise_logits, labels, name=name)
        cost = array_ops.reshape(cost, labels_shape)
        cost.set_shape(labels_static_shape)
        if logits.dtype == dtypes.float16:
            exit(math_ops.cast(cost, dtypes.float16))
        else:
            exit(cost)
