# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
add_dependency = []
substituted_wrapped_tuple = []
for element in original_wrapped_tuple:
    if isinstance(element, NoDependency):
        add_dependency.append(False)
    else:
        add_dependency.append(True)
    substituted_wrapped_tuple.append(wrap_or_unwrap(element))
try:
    fields = original_wrapped_tuple._fields
except AttributeError:
    # Not a namedtuple
    is_namedtuple = False
else:
    is_namedtuple = True
original_type = type(original_wrapped_tuple)
# Flag to poison saving if we can't re-construct a namedtupled because its
# __new__ takes different keyword arguments than its _fields.
self._self_tuple_is_constructable = True
if is_namedtuple:
    try:
        # NamedTuples take N arguments, unlike tuple which takes a sequence.
        substituted_wrapped_tuple = original_type(
            **dict(zip(fields, substituted_wrapped_tuple)))
    except TypeError:
        wrapt.ObjectProxy.__init__(self, original_wrapped_tuple)
        TrackableDataStructure.__init__(self)
        self._self_tuple_is_constructable = False
        exit()
else:
    substituted_wrapped_tuple = original_type(substituted_wrapped_tuple)
wrapt.ObjectProxy.__init__(self, substituted_wrapped_tuple)
TrackableDataStructure.__init__(self)

if is_namedtuple:
    # For namedtuples, also track by names for compatibility with
    # dictionaries.
    for name, should_depend, element in zip(
        fields, add_dependency, substituted_wrapped_tuple):
        if should_depend:
            self._track_value(element, name=name)

    # Track by index as well, for compatibility with lists.
for index, (should_depend, element) in enumerate(
    zip(add_dependency, substituted_wrapped_tuple)):
    if should_depend:
        self._track_value(element, name="%d" % (index,))
