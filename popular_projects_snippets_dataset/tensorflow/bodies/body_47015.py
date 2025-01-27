# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/policy.py
"""Constructs the policy.

    The `name` argument determines the compute and variable dtype, the default
    loss scale, and has no additional effect on the Policy. The compute and
    variable dtypes can only be specified through `name`, and cannot be
    specified directly.

    Args:
      name: A string. Can be one of the following values:
        * Any dtype name, such as 'float32' or 'float64'. Both the variable and
          compute dtypes will be that dtype.
        * 'mixed_float16' or 'mixed_bfloat16': The compute dtype is float16 or
          bfloat16, while the variable dtype is float32. With 'mixed_float16',
          a dynamic loss scale is used. These policies are used for mixed
          precision training.
      loss_scale: A `tf.compat.v1.mixed_precision.LossScale`, an int (which
        uses a `FixedLossScale`), the string "dynamic" (which uses a
        `DynamicLossScale`), or None (which uses no loss scale). Defaults to
        `"auto"`. In the `"auto"` case: 1) if `name` is `"mixed_float16"`, then
        use `loss_scale="dynamic"`. 2) otherwise, do not use a loss scale. Only
        `tf.keras.Model`s, not layers, use the loss scale, and it is only used
        during `Model.fit`, `Model.train_on_batch`, and other similar methods.
    """
super(PolicyV1, self).__init__(name)
if loss_scale == 'auto':
    loss_scale = 'dynamic' if name == 'mixed_float16' else None
    self._using_default_loss_scale = True
else:
    self._using_default_loss_scale = False
if loss_scale and self._compute_dtype not in (None, 'float16'):
    tf_logging.warning(
        'Creating a Policy with a loss scale is only useful for '
        'float16 policies. You passed loss_scale=%r for policy '
        '%s. Consider not passing any loss_scale instead.' %
        (loss_scale, name))
self._loss_scale = keras_loss_scale_module.get(loss_scale)
