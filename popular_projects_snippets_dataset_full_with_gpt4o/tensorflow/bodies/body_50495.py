# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(ProgbarLogger, self).__init__()
self._supports_tf_logs = True
if count_mode == 'samples':
    self.use_steps = False
elif count_mode == 'steps':
    self.use_steps = True
else:
    raise ValueError('Unknown `count_mode`: ' + str(count_mode))
# Defaults to all Model's metrics except for loss.
self.stateful_metrics = set(stateful_metrics) if stateful_metrics else set()

self.seen = 0
self.progbar = None
self.target = None
self.verbose = 1
self.epochs = 1

self._train_step, self._test_step, self._predict_step = None, None, None
self._call_batch_hooks = True

self._called_in_fit = False
