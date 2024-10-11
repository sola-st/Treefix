# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Conditionally creates batches of tensors based on `keep_input`.

  See docstring in `batch` for more details.

  Args:
    tensors: The list or dictionary of tensors to enqueue.
    keep_input: A `bool` Tensor.  This tensor controls whether the input is
      added to the queue or not.  If it is a scalar and evaluates `True`, then
      `tensors` are all added to the queue. If it is a vector and `enqueue_many`
      is `True`, then each example is added to the queue only if the
      corresponding value in `keep_input` is `True`. This tensor essentially
      acts as a filtering mechanism.
    batch_size: The new batch size pulled from the queue.
    num_threads: The number of threads enqueuing `tensors`.  The batching will
      be nondeterministic if `num_threads > 1`.
    capacity: An integer. The maximum number of elements in the queue.
    enqueue_many: Whether each tensor in `tensors` is a single example.
    shapes: (Optional) The shapes for each example.  Defaults to the
      inferred shapes for `tensors`.
    dynamic_pad: Boolean.  Allow variable dimensions in input shapes.
      The given dimensions are padded upon dequeue so that tensors within a
      batch have the same shapes.
    allow_smaller_final_batch: (Optional) Boolean. If `True`, allow the final
      batch to be smaller if there are insufficient items left in the queue.
    shared_name: (Optional). If set, this queue will be shared under the given
      name across multiple sessions.
    name: (Optional) A name for the operations.

  Returns:
    A list or dictionary of tensors with the same types as `tensors`.

  Raises:
    ValueError: If the `shapes` are not specified, and cannot be
      inferred from the elements of `tensors`.
  """
exit(_batch(
    tensors,
    batch_size,
    keep_input,
    num_threads=num_threads,
    capacity=capacity,
    enqueue_many=enqueue_many,
    shapes=shapes,
    dynamic_pad=dynamic_pad,
    allow_smaller_final_batch=allow_smaller_final_batch,
    shared_name=shared_name,
    name=name))
