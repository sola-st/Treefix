# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Creates a queue that dequeues elements in a first-in first-out order.

    A `FIFOQueue` has bounded capacity; supports multiple concurrent
    producers and consumers; and provides exactly-once delivery.

    A `FIFOQueue` holds a list of up to `capacity` elements. Each
    element is a fixed-length tuple of tensors whose dtypes are
    described by `dtypes`, and whose shapes are optionally described
    by the `shapes` argument.

    If the `shapes` argument is specified, each component of a queue
    element must have the respective fixed shape. If it is
    unspecified, different queue elements may have different shapes,
    but the use of `dequeue_many` is disallowed.

    Args:
      capacity: An integer. The upper bound on the number of elements
        that may be stored in this queue.
      dtypes:  A list of `DType` objects. The length of `dtypes` must equal
        the number of tensors in each queue element.
      shapes: (Optional.) A list of fully-defined `TensorShape` objects
        with the same length as `dtypes`, or `None`.
      names: (Optional.) A list of string naming the components in the queue
        with the same length as `dtypes`, or `None`.  If specified the dequeue
        methods return a dictionary with the names as keys.
      shared_name: (Optional.) If non-empty, this queue will be shared under
        the given name across multiple sessions.
      name: Optional name for the queue operation.
    """
dtypes = _as_type_list(dtypes)
shapes = _as_shape_list(shapes, dtypes)
names = _as_name_list(names, dtypes)
with ops.init_scope(), ops.device("CPU"):
    queue_ref = gen_data_flow_ops.fifo_queue_v2(
        component_types=dtypes,
        shapes=shapes,
        capacity=capacity,
        shared_name=_shared_name(shared_name),
        name=name)

super(FIFOQueue, self).__init__(dtypes, shapes, names, queue_ref)
