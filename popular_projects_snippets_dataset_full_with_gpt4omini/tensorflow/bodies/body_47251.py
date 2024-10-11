# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Build models on each replica."""
strategy = model._distribution_strategy

# If distributed_model is not built, create one for `mode`.
if model._compile_distribution:
    clone_model_on_replicas(model, strategy, mode)
else:
    _build_distributed_network(model, strategy, mode)
