# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/layer_utils.py
# type: (AttributeSentinel, str, bool) -> None
may_affect_upstream = self.attributes[key].mark_as(value)
if may_affect_upstream or self.always_propagate:
    for node in self._parents:  # type: AttributeSentinel
        node.invalidate(key)
