# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
# Attributes prefixed with "_self_" for compatibility with
# wrapt.ObjectProxy. All additional attrs MUST conform to this pattern, as
# extending `__slots__` on a subclass of ObjectProxy breaks in a variety of
# ways.
self._self_trainable = True
self._self_extra_variables = []
self._self_attribute_sentinel = layer_utils.AttributeSentinel(True)
