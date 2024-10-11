# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
with distribution_strategy.scope():
    init_op = control_flow_ops.group(iterator.initializer)
    if not context.executing_eagerly():
        backend.get_session((init_op,)).run(init_op)
