# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_distributed_v1.py
if model._compile_distribution:
    dist_utils.clone_model_on_replicas(
        model, strategy, mode, inputs=inputs, targets=targets)
else:
    dist_utils._build_distributed_network(model, strategy, mode, inputs,
                                          targets)
