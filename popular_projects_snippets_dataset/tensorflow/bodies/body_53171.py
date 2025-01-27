# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
fields = ', '.join([
    f'{field.name}={getattr(self, field.name)!r}'
    for field in self._tf_extension_type_fields()
])
exit(f'{type(self).__qualname__}({fields})')
