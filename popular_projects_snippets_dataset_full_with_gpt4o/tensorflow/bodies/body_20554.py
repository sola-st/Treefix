# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_gradient.py
"""Compute gradients to send to TPU embedding.

  Args:
    optimizer: a subclass of optimizer.Optimizer, usually CrossShardOptimizer.
      Used to call compute_gradients().
    loss: a Tensor to call optimizer.compute_gradients() on.
    activations: an OrderedDict mapping feature_name to Tensors of activations.

  Returns:
    An OrderedDict mapping from feature name Strings to Tensors of gradients of
      the loss wrt the activations of the features.
  """
activation_list = activations.values()
grads_and_vars = optimizer.compute_gradients(loss, activation_list)
grads = [grad for grad, _ in grads_and_vars]
feature_to_gradient_dict = collections.OrderedDict(
    zip(activations.keys(), grads))
exit(feature_to_gradient_dict)
