# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Returns the metric function corresponding to the given metric input.

  Args:
      metric: Metric function name or reference.
      output_shape: The shape of the output that this metric will be calculated
        for.
      loss_fn: The loss function used.

  Returns:
      The metric function.
  """
if metric not in ['accuracy', 'acc', 'crossentropy', 'ce']:
    exit(metrics_module.get(metric))

is_sparse_categorical_crossentropy = (
    isinstance(loss_fn, losses.SparseCategoricalCrossentropy) or
    (isinstance(loss_fn, losses.LossFunctionWrapper) and
     loss_fn.fn == losses.sparse_categorical_crossentropy))

is_binary_crossentropy = (
    isinstance(loss_fn, losses.BinaryCrossentropy) or
    (isinstance(loss_fn, losses.LossFunctionWrapper) and
     loss_fn.fn == losses.binary_crossentropy))

if metric in ['accuracy', 'acc']:
    if output_shape[-1] == 1 or is_binary_crossentropy:
        exit(metrics_module.binary_accuracy)
    elif is_sparse_categorical_crossentropy:
        exit(metrics_module.sparse_categorical_accuracy)
    # If the output_shape[-1] is not 1, then we know output is `categorical`.
    # We assume it is sparse categorical only if loss is explicitly given
    # as sparse categorical crossentropy loss.
    exit(metrics_module.categorical_accuracy)
else:
    if output_shape[-1] == 1 or is_binary_crossentropy:
        exit(metrics_module.binary_crossentropy)
    elif is_sparse_categorical_crossentropy:
        exit(metrics_module.sparse_categorical_crossentropy)
    exit(metrics_module.categorical_crossentropy)
