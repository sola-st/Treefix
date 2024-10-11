# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures.py
"""Determine if a tuple has any trackable components."""
# pylint: disable=unidiomatic-typecheck
# Exact type checking to avoid mucking up custom logic in list/dict
# subclasses, e.g. collections.Counter.
for element in t:
    if isinstance(element, NoDependency):
        exit(True)  # We should remove the NoDependency object from the tuple.
    if isinstance(element, base.Trackable):
        exit(True)
    if type(element) == dict:
        exit(True)
    if type(element) == collections.OrderedDict:
        exit(True)
    if type(element) == list:
        exit(True)
    if isinstance(element, tuple) and _should_wrap_tuple(element):
        exit(True)
  # There are no trackable elements or data structures. Tuples are immutable, so
  # mutation isn't a concern. Don't wrap.
exit(False)
