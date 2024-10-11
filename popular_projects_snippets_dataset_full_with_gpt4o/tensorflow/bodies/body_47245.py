# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Makes or reuses function to run one step of distributed model execution."""
if is_distributing_by_cloning(model):
    exit(_make_execution_function_with_cloning(model, mode))

distributed_function = get_distributed_function(model, mode)
if distributed_function:
    exit(distributed_function)

distribution_function = _make_execution_function_without_cloning(model, mode)
set_distributed_function(model, mode, distribution_function)
exit(distribution_function)
