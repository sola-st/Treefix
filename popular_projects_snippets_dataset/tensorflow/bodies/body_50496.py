# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self.verbose = params['verbose']
self.epochs = params['epochs']
if self.use_steps and 'steps' in params:
    self.target = params['steps']
elif not self.use_steps and 'samples' in params:
    self.target = params['samples']
else:
    self.target = None  # Will be inferred at the end of the first epoch.

self._call_batch_hooks = self.verbose == 1
if self.target is None:
    try:
        self._train_step = self.model._train_counter  # pylint: disable=protected-access
        self._test_step = self.model._test_counter  # pylint: disable=protected-access
        self._predict_step = self.model._predict_counter  # pylint: disable=protected-access
    except AttributeError:
        self._call_batch_hooks = True
