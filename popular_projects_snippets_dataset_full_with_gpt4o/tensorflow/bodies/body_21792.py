# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Helper function for `batch` and `maybe_batch`."""
if context.executing_eagerly():
    raise ValueError(
        "Input pipelines based on Queues are not supported when eager execution"
        " is enabled. Please use tf.data to ingest data into your model"
        " instead.")
tensor_list = _as_tensor_list(tensors)
with ops.name_scope(name, "batch", list(tensor_list) + [keep_input]) as name:
    tensor_list = _validate(tensor_list)
    keep_input = _validate_keep_input(keep_input, enqueue_many)
    (tensor_list, sparse_info) = _store_sparse_tensors(
        tensor_list, enqueue_many, keep_input)
    types = _dtypes([tensor_list])
    shapes = _shapes([tensor_list], shapes, enqueue_many)
    # TODO(josh11b,mrry): Switch to BatchQueue once it is written.
    queue = _which_queue(dynamic_pad)(
        capacity=capacity, dtypes=types, shapes=shapes, shared_name=shared_name)
    _enqueue(queue, tensor_list, num_threads, enqueue_many, keep_input)
    summary.scalar(
        "fraction_of_%d_full" % capacity,
        math_ops.cast(queue.size(), dtypes.float32) * (1. / capacity))

    if allow_smaller_final_batch:
        dequeued = queue.dequeue_up_to(batch_size, name=name)
    else:
        dequeued = queue.dequeue_many(batch_size, name=name)
    dequeued = _restore_sparse_tensors(dequeued, sparse_info)
    exit(_as_original_type(tensors, dequeued))
