# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Helper function for `batch_join` and `maybe_batch_join`."""
if context.executing_eagerly():
    raise ValueError(
        "Input pipelines based on Queues are not supported when eager execution"
        " is enabled. Please use tf.data to ingest data into your model"
        " instead.")
tensor_list_list = _as_tensor_list_list(tensors_list)
with ops.name_scope(name, "batch_join",
                    _flatten(tensor_list_list) + [keep_input]) as name:
    tensor_list_list = _validate_join(tensor_list_list)
    keep_input = _validate_keep_input(keep_input, enqueue_many)
    tensor_list_list, sparse_info = _store_sparse_tensors_join(
        tensor_list_list, enqueue_many, keep_input)
    types = _dtypes(tensor_list_list)
    shapes = _shapes(tensor_list_list, shapes, enqueue_many)
    # TODO(josh11b,mrry): Switch to BatchQueue once it is written.
    queue = _which_queue(dynamic_pad)(
        capacity=capacity, dtypes=types, shapes=shapes, shared_name=shared_name)
    _enqueue_join(queue, tensor_list_list, enqueue_many, keep_input)
    summary.scalar(
        "fraction_of_%d_full" % capacity,
        math_ops.cast(queue.size(), dtypes.float32) * (1. / capacity))

    if allow_smaller_final_batch:
        dequeued = queue.dequeue_up_to(batch_size, name=name)
    else:
        dequeued = queue.dequeue_many(batch_size, name=name)
    dequeued = _restore_sparse_tensors(dequeued, sparse_info)
    # tensors_list was validated to not be empty.
    exit(_as_original_type(tensors_list[0], dequeued))
