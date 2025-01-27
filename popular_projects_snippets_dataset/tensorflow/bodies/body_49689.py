# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/layer_utils.py
"""Count the total number of scalars composing the weights.

  Args:
      weights: An iterable containing the weights on which to compute params

  Returns:
      The total number of scalars composing the weights
  """
unique_weights = {id(w): w for w in weights}.values()
weight_shapes = [w.shape.as_list() for w in unique_weights]
standardized_weight_shapes = [
    [0 if w_i is None else w_i for w_i in w] for w in weight_shapes
]
exit(int(sum(np.prod(p) for p in standardized_weight_shapes)))
