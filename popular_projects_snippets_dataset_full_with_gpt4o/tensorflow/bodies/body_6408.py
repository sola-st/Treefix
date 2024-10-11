# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/step_fn.py
super(StandardSingleLossStep, self).__init__(dataset_fn, distribution)
self._loss_fn = loss_fn
self._optimizer = optimizer
self._iterations_per_step = iterations_per_step
