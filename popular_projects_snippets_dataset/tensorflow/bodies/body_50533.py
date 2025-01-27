# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(EarlyStopping, self).__init__()

self.monitor = monitor
self.patience = patience
self.verbose = verbose
self.baseline = baseline
self.min_delta = abs(min_delta)
self.wait = 0
self.stopped_epoch = 0
self.restore_best_weights = restore_best_weights
self.best_weights = None

if mode not in ['auto', 'min', 'max']:
    logging.warning('EarlyStopping mode %s is unknown, '
                    'fallback to auto mode.', mode)
    mode = 'auto'

if mode == 'min':
    self.monitor_op = np.less
elif mode == 'max':
    self.monitor_op = np.greater
else:
    if 'acc' in self.monitor:
        self.monitor_op = np.greater
    else:
        self.monitor_op = np.less

if self.monitor_op == np.greater:
    self.min_delta *= 1
else:
    self.min_delta *= -1
