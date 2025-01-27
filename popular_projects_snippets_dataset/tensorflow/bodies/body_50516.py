# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
logs = logs or {}
self.epoch.append(epoch)
for k, v in logs.items():
    self.history.setdefault(k, []).append(v)

# Set the history attribute on the model after the epoch ends. This will
# make sure that the state which is set is the latest one.
self.model.history = self
