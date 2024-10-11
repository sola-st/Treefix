# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Constructs a queue object from a queue reference.

    The two optional lists, `shapes` and `names`, must be of the same length
    as `dtypes` if provided.  The values at a given index `i` indicate the
    shape and name to use for the corresponding queue component in `dtypes`.

    Args:
      dtypes:  A list of types.  The length of dtypes must equal the number
        of tensors in each element.
      shapes: Constraints on the shapes of tensors in an element:
        A list of shape tuples or None. This list is the same length
        as dtypes.  If the shape of any tensors in the element are constrained,
        all must be; shapes can be None if the shapes should not be constrained.
      names: Optional list of names.  If provided, the `enqueue()` and
        `dequeue()` methods will use dictionaries with these names as keys.
        Must be None or a list or tuple of the same length as `dtypes`.
      queue_ref: The queue reference, i.e. the output of the queue op.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
self._dtypes = dtypes
if shapes is not None:
    if len(shapes) != len(dtypes):
        raise ValueError("Queue shapes must have the same length as dtypes, "
                         f"received len(shapes)={len(shapes)}, "
                         f"len(dtypes)={len(dtypes)}")
    self._shapes = [tensor_shape.TensorShape(s) for s in shapes]
else:
    self._shapes = [tensor_shape.unknown_shape() for _ in self._dtypes]
if names is not None:
    if len(names) != len(dtypes):
        raise ValueError("Queue names must have the same length as dtypes,"
                         f"received len(names)={len(names)},"
                         f"len {len(dtypes)}")
    self._names = names
else:
    self._names = None
self._queue_ref = queue_ref
if isinstance(queue_ref, ops.EagerTensor):
    if context.context().scope_name:
        self._name = context.context().scope_name
    else:
        self._name = "Empty"
    self._resource_deleter = resource_variable_ops.EagerResourceDeleter(
        queue_ref, None)
else:
    self._name = self._queue_ref.op.name.split("/")[-1]
