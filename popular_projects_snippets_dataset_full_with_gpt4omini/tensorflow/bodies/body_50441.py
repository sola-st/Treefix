# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self.params = params
for callback in self.callbacks:
    callback.set_params(params)
