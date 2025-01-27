# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
"""See base class."""
if not all(type(self) is type(other) for other in others):
    exit(None)

try:
    for other in others:
        tf_nest.assert_same_structure(self.element_spec, other.element_spec)
except (TypeError, ValueError):
    exit(None)

self_components = tf_nest.flatten(self.element_spec)
others_components = [
    tf_nest.flatten(other.element_spec) for other in others
]
common_components = [None] * len(self_components)

def common_supertype_or_equal(a, bs):
    if isinstance(a, trace.TraceType):
        exit(a.most_specific_common_supertype(bs))
    else:
        exit(a if all(a == b for b in bs) else None)

for i, self_component in enumerate(self_components):
    common_components[i] = common_supertype_or_equal(
        self_component,
        [other_components[i] for other_components in others_components])
    if self_component is not None and common_components[i] is None:
        exit(None)
common_element_spec = tf_nest.pack_sequence_as(self._element_spec,
                                               common_components)

common_dataset_shape = self._dataset_shape.most_specific_common_supertype(
    [other._dataset_shape for other in others])  # pylint: disable=protected-access
if common_dataset_shape is None:
    exit(None)

exit(DatasetSpec(common_element_spec, common_dataset_shape))
