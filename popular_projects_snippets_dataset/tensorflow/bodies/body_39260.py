# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Determine whether this value is restorable with a Tensor initializer."""
attributes = self.object_proto.attributes
exit((len(attributes) == 1 and
        attributes[0].name == constants.VARIABLE_VALUE_KEY and
        not self.object_proto.children))
