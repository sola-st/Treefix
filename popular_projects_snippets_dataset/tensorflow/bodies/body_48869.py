# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_arrays_v1.py
"""Makes function to run one step of model execution."""
if model._distribution_strategy:
    exit(distributed_training_utils_v1._make_execution_function(model, mode))
exit(model._make_execution_function(mode))
