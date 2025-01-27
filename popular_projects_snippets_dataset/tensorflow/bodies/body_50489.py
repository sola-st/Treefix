# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
super(BaseLogger, self).__init__()
self.stateful_metrics = set(stateful_metrics or [])
