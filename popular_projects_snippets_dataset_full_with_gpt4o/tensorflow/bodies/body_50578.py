# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(ReduceLROnPlateau, self).__init__()

self.monitor = monitor
if factor >= 1.0:
    raise ValueError('ReduceLROnPlateau ' 'does not support a factor >= 1.0.')
if 'epsilon' in kwargs:
    min_delta = kwargs.pop('epsilon')
    logging.warning('`epsilon` argument is deprecated and '
                    'will be removed, use `min_delta` instead.')
self.factor = factor
self.min_lr = min_lr
self.min_delta = min_delta
self.patience = patience
self.verbose = verbose
self.cooldown = cooldown
self.cooldown_counter = 0  # Cooldown counter.
self.wait = 0
self.best = 0
self.mode = mode
self.monitor_op = None
self._reset()
