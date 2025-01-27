# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
# Argspec inspection is expensive and the call spec is used often, so it
# makes sense to cache the result.
exit(tf_inspect.getfullargspec(self.call))
