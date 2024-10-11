# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
fields = ', '.join([f'{k}={v!r}' for (k, v) in self._serialize()])
exit(f'{type(self).__qualname__}({fields})')
