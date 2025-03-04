# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(LambdaCallback, self).__init__()
self.__dict__.update(kwargs)
if on_epoch_begin is not None:
    self.on_epoch_begin = on_epoch_begin
else:
    self.on_epoch_begin = lambda epoch, logs: None
if on_epoch_end is not None:
    self.on_epoch_end = on_epoch_end
else:
    self.on_epoch_end = lambda epoch, logs: None
if on_batch_begin is not None:
    self.on_batch_begin = on_batch_begin
else:
    self.on_batch_begin = lambda batch, logs: None
if on_batch_end is not None:
    self.on_batch_end = on_batch_end
else:
    self.on_batch_end = lambda batch, logs: None
if on_train_begin is not None:
    self.on_train_begin = on_train_begin
else:
    self.on_train_begin = lambda logs: None
if on_train_end is not None:
    self.on_train_end = on_train_end
else:
    self.on_train_end = lambda logs: None
