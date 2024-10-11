# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Validates the field annotations for tf.ExtensionType subclass `cls`."""
annotations = getattr(cls, '__annotations__', {})

# Check that no fields use reserved names.
for name, value in cls.__dict__.items():
    if name == 'Spec':
        if not isinstance(value, type):
            raise ValueError(f'{cls.__qualname__}.Spec must be a nested class; '
                             f'got {value}.')
        if (value.__bases__ != (type_spec.TypeSpec,) and value.__bases__ !=
            (object,)):
            raise ValueError(f'{cls.__qualname__}.Spec must be directly subclassed '
                             'from tf.TypeSpec.')
    elif extension_type_field.ExtensionTypeField.is_reserved_name(name):
        raise ValueError(f'The field annotations for {cls.__name__} are '
                         f"invalid. Field '{name}' is reserved.")
for name in annotations:
    if extension_type_field.ExtensionTypeField.is_reserved_name(name):
        raise ValueError(f'The field annotations for {cls.__name__} are '
                         f"invalid. Field '{name}' is reserved.")

  # Check that all fields have type annotaitons.
for (key, value) in cls.__dict__.items():
    if not (key in annotations or callable(value) or key.startswith('_abc_') or
            key == '_tf_extension_type_fields' or
            key.startswith('__') and key.endswith('__') or
            isinstance(value, (property, classmethod, staticmethod))):
        raise ValueError(f'The field annotations for {cls.__name__} are '
                         f'invalid. Field {key} is missing a type annotation.')
