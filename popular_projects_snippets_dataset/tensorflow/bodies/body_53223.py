# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""Creates a nested TypeSpec class for tf.ExtensionType subclass `cls`."""
spec_name = cls.__name__ + '.Spec'
spec_qualname = cls.__qualname__ + '.Spec'

# Set __module__ explicitly as a dynamic created class has module='abc'
# by default.
spec_dict = {'value_type': cls, '__module__': cls.__module__}

# Copy user-supplied customizations into the TypeSpec.
user_spec = cls.__dict__.get('Spec', None)
if user_spec is not None:
    for (name, value) in user_spec.__dict__.items():
        if extension_type_field.ExtensionTypeField.is_reserved_name(name):
            raise ValueError(f'TypeSpec {spec_qualname} uses reserved '
                             f"name '{name}'.")
        if cls._tf_extension_type_has_field(name):  # pylint: disable=protected-access
            raise ValueError(f"TypeSpec {spec_qualname} defines a variable '{name}'"
                             f' which shadows a field in {cls.__qualname__}')
        if name in ('__module__', '__dict__', '__weakref__'):
            continue

        spec_dict[name] = value

if issubclass(cls, BatchableExtensionType):
    type_spec_base = BatchableExtensionTypeSpec
    if hasattr(cls,
               '__batch_encoder__') and '__batch_encoder__' not in spec_dict:
        spec_dict['__batch_encoder__'] = cls.__batch_encoder__
else:
    type_spec_base = ExtensionTypeSpec
    if hasattr(cls, '__batch_encoder__') or '__batch_encoder__' in spec_dict:
        raise ValueError('__batch_encoder__ should only be defined for '
                         'BatchableExtensionType classes.')

  # Build the TypeSpec and store it as a nested class inside `cls`.
spec = type(spec_name, (type_spec_base,), spec_dict)
spec.__qualname__ = spec_qualname
setattr(cls, 'Spec', spec)

# Build a constructor for the TypeSpec class.
if '__init__' in spec.__dict__:
    _wrap_user_constructor(spec)
else:
    _build_spec_constructor(spec)

cls.__abstractmethods__ -= {'_type_spec'}

# If the user included an explicit `__name__` attribute, then use that to
# register the TypeSpec (so it can be used in SavedModel signatures).
if '__name__' in cls.__dict__:
    type_spec.register(cls.__dict__['__name__'] + '.Spec')(spec)
