# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/losses.py
"""Handles `AUTO` reduction cases and returns the reduction value."""
if (not self._allow_sum_over_batch_size and
    distribution_strategy_context.has_strategy() and
    (self.reduction == losses_utils.ReductionV2.AUTO or
     self.reduction == losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE)):
    raise ValueError(
        'Please use `tf.keras.losses.Reduction.SUM` or '
        '`tf.keras.losses.Reduction.NONE` for loss reduction when losses are '
        'used with `tf.distribute.Strategy` outside of the built-in training '
        'loops. You can implement '
        '`tf.keras.losses.Reduction.SUM_OVER_BATCH_SIZE` using global batch '
        'size like:\n```\nwith strategy.scope():\n'
        '    loss_obj = tf.keras.losses.CategoricalCrossentropy('
        'reduction=tf.keras.losses.Reduction.NONE)\n....\n'
        '    loss = tf.reduce_sum(loss_obj(labels, predictions)) * '
        '(1. / global_batch_size)\n```\nPlease see '
        'https://www.tensorflow.org/tutorials/distribute/custom_training'
        ' for more details.')

if self.reduction == losses_utils.ReductionV2.AUTO:
    exit(losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE)
exit(self.reduction)
