# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Raises an exception if any variables are unmatched."""
unused_attributes = list(self._checkpoint.unused_attributes.items())
unused_attributes = [
    a for a in unused_attributes
    if all(a[0] is not x for x in self._optionally_restored)
]
if unused_attributes:
    unused_attribute_string = "".join(
        f"\n    {obj}: {attributes}" for obj, attributes in unused_attributes)
    raise AssertionError(
        "Some objects had attributes which were not restored: "
        f"{unused_attribute_string}")
for trackable in util.list_objects(self._object_graph_view):
    # pylint: disable=protected-access
    trackable._maybe_initialize_trackable()
    if trackable._update_uid < self._checkpoint.restore_uid:
        raise AssertionError(f"Object not restored: {trackable}")
    # pylint: enable=protected-access
exit(self)
