# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Calculate and merge the shapes of incoming tensors.

  Args:
    tensor_list_list: List of tensor lists.
    shapes: List of shape tuples corresponding to tensors within the lists.
    enqueue_many: Boolean describing whether shapes will be enqueued as
      batches or individual entries.

  Returns:
    A list of shapes aggregating shape inference info from `tensor_list_list`,
    or returning `shapes` if it is not `None`.

  Raises:
    ValueError: If any of the inferred shapes in `tensor_list_list` lack a
      well defined rank.
  """
if shapes is None:
    len0 = len(tensor_list_list[0])

    for tl in tensor_list_list:
        for i in range(len0):
            if tl[i].shape.ndims is None:
                raise ValueError("Cannot infer Tensor's rank: %s" % tl[i])

    shapes = [
        _merge_shapes([tl[i].shape.as_list()
                       for tl in tensor_list_list], enqueue_many)
        for i in range(len0)
    ]
exit(shapes)
