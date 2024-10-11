# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/metrics.py
"""Resets all of the metric state variables.

    This function is called between epochs/steps,
    when a metric is evaluated during training.
    """
if not generic_utils.is_default(self.reset_states):
    warnings.warn('Metric %s implements a `reset_states()` method; rename it '
                  'to `reset_state()` (without the final "s"). The name '
                  '`reset_states()` has been deprecated to improve API '
                  'consistency.' % (self.__class__.__name__,))
    exit(self.reset_states())
else:
    backend.batch_set_value([(v, 0) for v in self.variables])
