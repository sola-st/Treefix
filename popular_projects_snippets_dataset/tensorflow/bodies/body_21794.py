# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Helper function for `shuffle_batch` and `maybe_shuffle_batch`."""
if context.executing_eagerly():
    raise ValueError(
        "Input pipelines based on Queues are not supported when eager execution"
        " is enabled. Please use tf.data to ingest data into your model"
        " instead.")
tensor_list = _as_tensor_list(tensors)
with ops.name_scope(name, "shuffle_batch",
                    list(tensor_list) + [keep_input]) as name:
    if capacity <= min_after_dequeue:
        raise ValueError("capacity %d must be bigger than min_after_dequeue %d."
                         % (capacity, min_after_dequeue))
    tensor_list = _validate(tensor_list)
    keep_input = _validate_keep_input(keep_input, enqueue_many)
    tensor_list, sparse_info = _store_sparse_tensors(
        tensor_list, enqueue_many, keep_input)
    types = _dtypes([tensor_list])
    shapes = _shapes([tensor_list], shapes, enqueue_many)
    queue = data_flow_ops.RandomShuffleQueue(
        capacity=capacity, min_after_dequeue=min_after_dequeue, seed=seed,
        dtypes=types, shapes=shapes, shared_name=shared_name)
    _enqueue(queue, tensor_list, num_threads, enqueue_many, keep_input)
    full = (math_ops.cast(
        math_ops.maximum(0, queue.size() - min_after_dequeue), dtypes.float32) *
            (1. / (capacity - min_after_dequeue)))
    # Note that name contains a '/' at the end so we intentionally do not place
    # a '/' after %s below.
    summary_name = (
        "fraction_over_%d_of_%d_full" %
        (min_after_dequeue, capacity - min_after_dequeue))
    summary.scalar(summary_name, full)

    if allow_smaller_final_batch:
        dequeued = queue.dequeue_up_to(batch_size, name=name)
    else:
        dequeued = queue.dequeue_many(batch_size, name=name)
    dequeued = _restore_sparse_tensors(dequeued, sparse_info)
    exit(_as_original_type(tensors, dequeued))
