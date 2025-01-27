# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
self._prefix = prefix
self._local_names = local_names
self._trackable = obj
self._call_with_mapped_captures = call_with_mapped_captures
super(TrackableSaveable, self).__init__(obj, specs, name)
