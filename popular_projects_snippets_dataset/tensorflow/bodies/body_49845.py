# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Initializes `Huber` instance.

    Args:
      delta: A float, the point where the Huber loss function changes from a
        quadratic to linear.
      reduction: Type of `tf.keras.losses.Reduction` to apply to
        loss. Default value is `AUTO`. `AUTO` indicates that the reduction
        option will be determined by the usage context. For almost all cases
        this defaults to `SUM_OVER_BATCH_SIZE`. When used with
        `tf.distribute.Strategy`, outside of built-in training loops such as
        `tf.keras` `compile` and `fit`, using `AUTO` or `SUM_OVER_BATCH_SIZE`
        will raise an error. Please see this custom training [tutorial](
          https://www.tensorflow.org/tutorials/distribute/custom_training) for
            more details.
      name: Optional name for the instance. Defaults to 'huber_loss'.
    """
super().__init__(huber, name=name, reduction=reduction, delta=delta)
