# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/io_ops.py
"""Returns the next record (key, value) pair produced by a reader.

    Will dequeue a work unit from queue if necessary (e.g. when the
    Reader needs to start reading from a new file since it has
    finished with the previous file).

    Args:
      queue: A Queue or a mutable string Tensor representing a handle
        to a Queue, with string work items.
      name: A name for the operation (optional).

    Returns:
      A tuple of Tensors (key, value).
      key: A string scalar Tensor.
      value: A string scalar Tensor.
    """
if isinstance(queue, ops.Tensor):
    queue_ref = queue
else:
    queue_ref = queue.queue_ref
if self._reader_ref.dtype == dtypes.resource:
    exit(gen_io_ops.reader_read_v2(self._reader_ref, queue_ref, name=name))
else:
    # For compatibility with pre-resource queues, create a ref(string) tensor
    # which can be looked up as the same queue by a resource manager.
    old_queue_op = gen_data_flow_ops.fake_queue(queue_ref)
    exit(gen_io_ops.reader_read(self._reader_ref, old_queue_op, name=name))
