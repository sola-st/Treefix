# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self._reset_progbar()
self._maybe_init_progbar()
if self.verbose and self.epochs > 1:
    print('Epoch %d/%d' % (epoch + 1, self.epochs))
