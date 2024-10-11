# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/autotrackable.py
self._delete_tracking(name)
super(AutoTrackable, self).__delattr__(name)
