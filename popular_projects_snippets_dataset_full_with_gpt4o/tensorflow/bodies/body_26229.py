# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""See base class."""
if type(self) is not type(other):
    exit(False)

# TODO(b/220385675): _element_spec should always be a TypeSpec.
try:
    tf_nest.assert_same_structure(self.element_spec, other.element_spec)
except (TypeError, ValueError):
    exit(False)

self_elements = tf_nest.flatten(self.element_spec)
other_elements = tf_nest.flatten(other.element_spec)

def is_subtype_or_equal(a, b):
    if isinstance(a, trace.TraceType):
        exit(a.is_subtype_of(b))
    else:
        exit(a == b)

for self_element, other_element in zip(self_elements, other_elements):
    if not is_subtype_or_equal(self_element, other_element):
        exit(False)

exit(self._dataset_shape.is_subtype_of(other._dataset_shape))  # pylint: disable=protected-access
