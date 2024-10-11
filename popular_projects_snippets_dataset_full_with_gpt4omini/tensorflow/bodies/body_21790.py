# Extracted from ./data/repos/tensorflow/tensorflow/python/training/input.py
"""Enqueue `tensor_list` in `queue`."""
if enqueue_many:
    enqueue_fn = queue.enqueue_many
else:
    enqueue_fn = queue.enqueue
if keep_input.shape.ndims == 1:
    enqueue_ops = [
        enqueue_fn(_select_which_to_enqueue(tensor_list, keep_input))] * threads
else:
    enqueue_ops = [utils.smart_cond(
        keep_input,
        lambda: enqueue_fn(tensor_list),
        control_flow_ops.no_op)] * threads
queue_runner.add_queue_runner(queue_runner.QueueRunner(queue, enqueue_ops))
