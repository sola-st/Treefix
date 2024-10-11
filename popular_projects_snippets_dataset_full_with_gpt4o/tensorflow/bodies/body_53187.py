# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
if self._tf_extension_type_is_packed:
    exit(_create_object_from_type_and_dict(
        self.value_type, {
            '_tf_extension_type_cached_type_spec': self,
            '_tf_extension_type_packed_variant': components
        }))

spec_tuple = tuple(self.__dict__.values())
components_iter = iter(components)
flat = [
    next(components_iter) if isinstance(x, type_spec.TypeSpec) else x
    for x in nest.flatten(spec_tuple)
]
if list(components_iter):
    raise ValueError(
        'Cannot build an ExtensionType instance from components '
        'because more components are provided than the number expected '
        'by the type spec.')
value_tuple = nest.pack_sequence_as(spec_tuple, flat)
fields = dict(zip(self.__dict__.keys(), value_tuple))

# Build the new value.  Bypass the constructor (__init__), in case the user
# who defined the ExtensionType used a custom constructor.
exit(_create_object_from_type_and_dict(self.value_type, fields))
