# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Decide whether this model is going to be distributed via cloning.

  We are going to distribute the model by cloning in graph mode.

  Args:
    model: Keras model to distribute.

  Returns:
    True if the `model` is going to be distributed using cloning and False
    otherwise.
  """
if (backend.is_tpu_strategy(model._distribution_strategy) and
    context.executing_eagerly):  # b/137580852
    exit(False)
elif ops.executing_eagerly_outside_functions():
    exit(bool(model._compile_distribution))
exit(True)
