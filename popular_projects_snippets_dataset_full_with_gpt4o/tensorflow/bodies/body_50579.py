# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Resets wait counter and cooldown counter.
    """
if self.mode not in ['auto', 'min', 'max']:
    logging.warning('Learning rate reduction mode %s is unknown, '
                    'fallback to auto mode.', self.mode)
    self.mode = 'auto'
if (self.mode == 'min' or
    (self.mode == 'auto' and 'acc' not in self.monitor)):
    self.monitor_op = lambda a, b: np.less(a, b - self.min_delta)
    self.best = np.Inf
else:
    self.monitor_op = lambda a, b: np.greater(a, b + self.min_delta)
    self.best = -np.Inf
self.cooldown_counter = 0
self.wait = 0
