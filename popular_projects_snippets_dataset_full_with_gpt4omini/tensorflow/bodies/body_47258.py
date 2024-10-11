# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Copies weights from first distributed model back to original model."""
if model._distribution_strategy and mode == ModeKeys.TRAIN:
    distributed_model = get_distributed_model(model, mode)
    updated_weights = model._distribution_strategy.unwrap(
        distributed_model)[0].get_weights()
    model.set_weights(updated_weights)
