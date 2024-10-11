# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Copies weights from original model to distributed models."""
strategy = original_model._distribution_strategy
distributed_model = get_distributed_model(original_model, mode)
if strategy:
    # Copy the weights from the original model to each of the replicated
    # models.
    orig_model_weights = original_model.get_weights()
    first_model = strategy.unwrap(distributed_model)[0]
    set_weights(strategy, first_model, orig_model_weights)
