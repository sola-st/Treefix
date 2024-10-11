# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/loss_scale_optimizer.py
if not isinstance(opt, optimizer.Optimizer):
    raise ValueError('"opt" must be an instance of Optimizer, but got: %s' %
                     type(opt))
self._optimizer = opt

use_locking = opt._use_locking  # pylint: disable=protected-access
name = opt.get_name()
super(MixedPrecisionLossScaleOptimizer, self).__init__(use_locking, name)

self._loss_scale = loss_scale_module.get(loss_scale)
if self._loss_scale is None:
    raise ValueError('loss_scale cannot be None')
self._track_trackable(self._optimizer, 'base_optimizer')
self._track_trackable(self._loss_scale, 'loss_scale')
