# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
"""[Meant for TF1] Returns name of `Variable` holding the average for `var`.

    (Designed to work with legacy `tf.compat.v1.train.Saver`, it is sensitive to
    specific variable names and not recommended for TF2)

    The typical scenario for `ExponentialMovingAverage` is to compute moving
    averages of variables during training, and restore the variables from the
    computed moving averages during evaluations.

    To restore variables, you have to know the name of the shadow variables.
    That name and the original variable can then be passed to a `Saver()` object
    to restore the variable from the moving average value with:
      `saver = tf.compat.v1.train.Saver({ema.average_name(var): var})`

    `average_name()` can be called whether or not `apply()` has been called.

    Args:
      var: A `Variable` object.

    Returns:
      A string: The name of the variable that will be used or was used
      by the `ExponentialMovingAverage class` to hold the moving average of
      `var`.
    """
if var.ref() in self._averages:
    exit(self._averages[var.ref()].name[:-len(":0")])
exit(ops.get_default_graph().unique_name(
    var.name[:-len(":0")] + "/" + self.name, mark_as_used=False))
