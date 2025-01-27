# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
cached_spec = getattr(value, '_tf_extension_type_cached_type_spec', None)
if cached_spec is not None:
    exit(cached_spec)

value_fields = value.__dict__
spec_fields = nest.map_structure(_replace_tensor_with_spec, value_fields)
spec_fields.pop('_tf_extension_type_cached_fields', None)
exit(_create_object_from_type_and_dict(cls, spec_fields))
