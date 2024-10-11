# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
state['_thread_local'] = threading.local()
state['_metrics_lock'] = threading.Lock()
# Bypass Trackable logic as `__dict__` already contains this info.
object.__setattr__(self, '__dict__', state)
