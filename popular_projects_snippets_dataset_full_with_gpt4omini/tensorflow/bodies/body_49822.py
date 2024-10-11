# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Initializes `Loss` class.

    Args:
      reduction: Type of `tf.keras.losses.Reduction` to apply to
        loss. Default value is `AUTO`. `AUTO` indicates that the reduction
        option will be determined by the usage context. For almost all cases
        this defaults to `SUM_OVER_BATCH_SIZE`. When used with
        `tf.distribute.Strategy`, outside of built-in training loops such as
        `tf.keras` `compile` and `fit`, using `AUTO` or `SUM_OVER_BATCH_SIZE`
        will raise an error. Please see this custom training [tutorial](
          https://www.tensorflow.org/tutorials/distribute/custom_training) for
            more details.
      name: Optional name for the instance.
    """
losses_utils.ReductionV2.validate(reduction)
self.reduction = reduction
self.name = name
# SUM_OVER_BATCH is only allowed in losses managed by `fit` or
# CannedEstimators.
self._allow_sum_over_batch_size = False
self._set_name_scope()
