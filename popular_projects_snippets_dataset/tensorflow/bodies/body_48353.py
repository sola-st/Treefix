# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
state['_thread_local'] = threading.local()
# Bypass Trackable logic as `__dict__` already contains this info.
object.__setattr__(self, '__dict__', state)
