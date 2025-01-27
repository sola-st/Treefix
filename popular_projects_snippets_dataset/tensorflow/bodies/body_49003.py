# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Override to support `copy.deepcopy` and pickling.
# Thread-local objects cannot be copied in Python 3, so pop these.
# Thread-local objects are used to cache losses in MirroredStrategy, and
# so shouldn't be copied.
state = self.__dict__.copy()
state.pop('_thread_local', None)
state.pop('_metrics_lock', None)
exit(state)
