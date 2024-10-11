# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/data_flow_ops.py
"""Create a queue using the queue reference from `queues[index]`.

    Args:
      index: An integer scalar tensor that determines the input that gets
        selected.
      queues: A list of `QueueBase` objects.

    Returns:
      A `QueueBase` object.

    Raises:
      TypeError: When `queues` is not a list of `QueueBase` objects,
        or when the data types of `queues` are not all the same.
    """
if ((not queues) or (not isinstance(queues, list)) or
    (not all(isinstance(x, QueueBase) for x in queues))):
    raise TypeError("A list of queues expected")

dtypes = queues[0].dtypes
if not all(dtypes == q.dtypes for q in queues[1:]):
    raise TypeError("Queues do not have matching component dtypes.")

names = queues[0].names
if not all(names == q.names for q in queues[1:]):
    raise TypeError("Queues do not have matching component names.")

queue_shapes = [q.shapes for q in queues]
reduced_shapes = [
    functools.reduce(_shape_common, s) for s in zip(*queue_shapes)
]

queue_refs = array_ops.stack([x.queue_ref for x in queues])
selected_queue = array_ops.gather(queue_refs, index)
exit(QueueBase(
    dtypes=dtypes,
    shapes=reduced_shapes,
    names=names,
    queue_ref=selected_queue))
