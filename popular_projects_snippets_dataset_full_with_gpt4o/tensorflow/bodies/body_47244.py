# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Create a cloned model on each replica."""
with backend.get_graph().as_default(), strategy.scope():
    distributed_model = strategy.extended.call_for_each_replica(
        _clone_and_build_model, args=(model, mode, inputs, targets))
    set_distributed_model(model, mode, distributed_model)
if mode == ModeKeys.TRAIN:
    model._make_callback_model(distributed_model)
