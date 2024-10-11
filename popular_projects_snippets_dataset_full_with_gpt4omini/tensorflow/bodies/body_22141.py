# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision.py
"""Registers a loss scale optimizer wrapper.

  `tf.compat.v1.mixed_precision.enable_mixed_precision_graph_rewrite`
  automatically wraps an optimizer with an optimizer wrapper that performs loss
  scaling. This function registers a
  `(base_cls, wrapper_fn, wrapper_cls)` triple
  that is used by `enable_mixed_precision_graph_rewrite`, where
  `wrapper_fn` is called to create a `wrapper_cls` instance that wraps an
  `optimizer_cls` instance.

  Args:
    optimizer_cls: A base optimizer class, e.g. `tf.keras.optimizers.Optimizer`.
    wrapper_fn: A function that takes in arguments "optimizer" and
      "loss_scale", and returns a loss scale optimizer of type "wrapper_cls"
      that wraps "optimizer".
    wrapper_cls: A loss scale optimizer class. Defaults to `wrapper_fn`, in
      which case `wrapper_fn` should be a loss scale optimizer class whose
      constructor takes in arguments "optimizer" and "loss_scale".
  """
_REGISTERED_WRAPPER_OPTIMIZER_CLS[optimizer_cls] = (
    wrapper_fn, wrapper_cls or wrapper_fn)
