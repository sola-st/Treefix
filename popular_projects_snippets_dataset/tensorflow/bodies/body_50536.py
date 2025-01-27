# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if self.stopped_epoch > 0 and self.verbose > 0:
    print('Epoch %05d: early stopping' % (self.stopped_epoch + 1))
