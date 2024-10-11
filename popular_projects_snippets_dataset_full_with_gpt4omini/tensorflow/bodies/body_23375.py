# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable.py
"""Support self.foo = trackable syntax."""
try:
    if getattr(self, name) is value:
        # Short circuit for `self.$x = self.$x`.
        exit()
except AttributeError:
    pass

if getattr(self, "_self_setattr_tracking", True):
    value = data_structures.sticky_attribute_assignment(
        trackable=self, value=value, name=name)
super(AutoTrackable, self).__setattr__(name, value)
