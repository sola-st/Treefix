# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
if wrapped_dict is None:
    # Allow zero-argument construction, e.g. from session.run's re-wrapping.
    wrapped_dict = {}
if not isinstance(wrapped_dict, collections_abc.Mapping):
    # Allow construction from a sequence, e.g. from nest.pack_sequence_as.
    wrapped_dict = dict(wrapped_dict)
wrapt.ObjectProxy.__init__(self, wrapped_dict)
TrackableDataStructure.__init__(self)
self._self_non_string_key = False
self._self_external_modification = False
self.__wrapped__.update(
    {key: self._track_value(
        value, name=self._name_element(key))
     for key, value in self.__wrapped__.items()})
self._update_snapshot()
