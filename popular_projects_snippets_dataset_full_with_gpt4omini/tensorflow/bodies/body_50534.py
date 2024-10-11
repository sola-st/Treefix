# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
# Allow instances to be re-used
self.wait = 0
self.stopped_epoch = 0
self.best = np.Inf if self.monitor_op == np.less else -np.Inf
self.best_weights = None
