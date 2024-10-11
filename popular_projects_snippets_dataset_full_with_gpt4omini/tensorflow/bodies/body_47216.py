# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Sets the weights of the replicated models.

  The weights of the replicated models are set to the weights of the original
  model. The weights of the replicated model are Mirrored variables and hence
  we need to use the `update` call within a DistributionStrategy scope.

  Args:
    distribution_strategy: DistributionStrategy used to distribute training
        and validation.
    dist_model: The replicated models on the different devices.
    weights: The weights of the original model.
  """
assign_ops = []
for layer in dist_model.layers:
    num_param = len(layer.weights)
    layer_weights = weights[:num_param]
    for sw, w in zip(layer.weights, layer_weights):
        if ops.executing_eagerly_outside_functions():
            sw.assign(w)
        else:
            assign_ops.append(distribution_strategy.unwrap(sw.assign(w)))
    weights = weights[num_param:]

if not ops.executing_eagerly_outside_functions():
    backend.get_session(assign_ops).run(assign_ops)
