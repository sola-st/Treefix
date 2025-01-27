# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self.model = model
if self._history:
    model.history = self._history
for callback in self.callbacks:
    callback.set_model(model)
