# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options.py
if not self._mutable:
    raise ValueError("Mutating `tf.data.Options()` returned by "
                     "`tf.data.Dataset.options()` has no effect. Use "
                     "`tf.data.Dataset.with_options(options)` to set or "
                     "update dataset options.")
if hasattr(self, name):
    object.__setattr__(self, name, value)
else:
    raise AttributeError("Cannot set the property {} on {}.".format(
        name,
        type(self).__name__))
