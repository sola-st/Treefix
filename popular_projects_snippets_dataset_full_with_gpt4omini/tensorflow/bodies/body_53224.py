# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
for name in fields:
    if (extension_type_field.ExtensionTypeField.is_reserved_name(name) or
        (name.startswith('__') and name.endswith('__'))):
        raise ValueError(
            f'Reserved field name {name} was encountered '
            f'when trying to instantiate an AnonymousExtensionType.')
fields = [(k, _convert_anonymous_fields(v)) for (k, v) in fields.items()]
self.__dict__.update(fields)
self._tf_extension_type_convert_fields()
super().__init__()
