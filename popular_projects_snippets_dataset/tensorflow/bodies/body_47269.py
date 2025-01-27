# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Update sample_weight_mode of the distributed model."""
if is_distributing_by_cloning(model):
    distributed_model = get_distributed_model(model, mode)
    if not distributed_model:
        _make_replicated_models_with_cloning(model, mode)
        distributed_model = get_distributed_model(model, mode)
    distributed_model._recompile_exec_function = any(
        [e.sample_weights_mismatch() for e in model._training_endpoints])

    if sample_weights:
        distributed_models = flatten_per_replica_values(
            model._distribution_strategy, distributed_model)
        # sample_weights is a tuple of 1 list where the number of elements in the
        # list is equal to the number of replicas in sync.
        sample_weights = sample_weights[0]
        if sample_weights and None not in sample_weights:
            for m, sw in zip(distributed_models, sample_weights):
                m._update_sample_weight_modes(sample_weights=[sw])
