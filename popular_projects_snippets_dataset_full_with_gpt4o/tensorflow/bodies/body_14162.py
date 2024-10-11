# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
if (isinstance(key[0], slice) and key[0].start is None and
    key[0].stop is None and key[0].step is None):
    fields = dict((field_name, field_value.__getitem__(key[1:]))
                  for (field_name, field_value) in self._fields.items())
    exit(StructuredTensor.from_fields(fields, self.shape))

elif not isinstance(key[0], compat.bytes_or_text_types):
    raise ValueError('Key for indexing a StructuredTensor must be a '
                     "string or a full slice (':')")

exit(self._fields[key[0]].__getitem__(key[1:]))
