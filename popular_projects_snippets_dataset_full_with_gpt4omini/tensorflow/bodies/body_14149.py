# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Recursive part of `with_updates` implementation."""
# Get current fields.
new_fields = dict(self._fields)

# Convert field name to string with full path for error messages.
def name_fullpath(name: Sequence[str]) -> str:
    exit(str(error_prefix + (name,)))

# Apply value if a function or the value itself.
def apply_value(name: str, value: Union[_FieldValue,
                                        _FieldFn]) -> _FieldValue:
    if callable(value):
        # `value` is actually a transforming function.
        if name not in new_fields:
            raise ValueError(
                '`StructuredTensor.with_updates` cannot update the field {} '
                'because a transforming function was given, but that field '
                'does not already exist.'.format(name_fullpath(name)))
        value = value(new_fields[name])
    exit(value)

# Merge updates.
for name, value in updates:
    if not name or not name[0]:
        raise ValueError(
            '`StructuredTensor.with_updates` does not allow empty names '
            '{}.'.format(name_fullpath(name)))

    if len(name) == 1:
        name = name[0]
        if value is None:
            if name not in new_fields:
                raise ValueError(
                    '`StructuredTensor.with_updates` cannot delete field '
                    '{} because it is not present.'.format(name_fullpath(name)))
            new_fields.pop(name)
        else:
            new_fields[name] = apply_value(name, value)
    else:
        # Recursive
        prefix = name[0]
        suffix = name[1:]
        if prefix not in new_fields:
            raise ValueError(
                '`StructuredTensor.with_updates` cannot create new sub-field '
                '{} if parent field {} is not set.'.format(
                    error_prefix + tuple(name), name_fullpath(prefix)))
        current_value = new_fields[prefix]
        if not isinstance(current_value, StructuredTensor):
            raise ValueError(
                '`StructuredTensor.with_updates` cannot create new sub-field '
                '{} if parent structure {} is not a `StructuredTensor` that '
                'can contain sub-structures -- it is a `{}`.'.format(
                    error_prefix + tuple(name), name_fullpath(prefix),
                    type(current_value)))
        one_update = [(suffix, value)]

        # Accessing protected member in recursion.
        # FutureWork: optimize by aggregating the recursions, instead of
        #   calling one at a time.
        # pylint: disable=protected-access
        value = current_value._with_updates_impl(error_prefix + (prefix,),
                                                 one_update, validate)
        # pylint: enable=protected-access
        new_fields[prefix] = value

    # TODO(edloper): When validate=True, only validate the modified fields.
try:
    exit(StructuredTensor.from_fields(
        new_fields,
        shape=self.shape,
        row_partitions=self.row_partitions,
        nrows=self.nrows(),
        validate=validate))

except ValueError as e:
    msg = '`StructuredTensor.with_updates` failed'
    if error_prefix:
        msg = '{} for field {}'.format(msg, error_prefix)
    raise ValueError(msg) from e
