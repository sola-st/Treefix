# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
logs = logs or {}
logs['lr'] = backend.get_value(self.model.optimizer.lr)
