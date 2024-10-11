# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if not hasattr(self.model.optimizer, 'lr'):
    raise ValueError('Optimizer must have a "lr" attribute.')
try:  # new API
    lr = float(backend.get_value(self.model.optimizer.lr))
    lr = self.schedule(epoch, lr)
except TypeError:  # Support for old API for backward compatibility
    lr = self.schedule(epoch)
if not isinstance(lr, (ops.Tensor, float, np.float32, np.float64)):
    raise ValueError('The output of the "schedule" function '
                     'should be float.')
if isinstance(lr, ops.Tensor) and not lr.dtype.is_floating:
    raise ValueError('The dtype of Tensor should be float')
backend.set_value(self.model.optimizer.lr, backend.get_value(lr))
if self.verbose > 0:
    print('\nEpoch %05d: LearningRateScheduler setting learning '
          'rate to %s.' % (epoch + 1, lr))
