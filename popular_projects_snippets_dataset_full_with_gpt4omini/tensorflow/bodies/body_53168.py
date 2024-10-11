# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
"""An ordered list describing the fields of this ExtensionType.

    Returns:
      A list of `ExtensionTypeField` objects.  Forward references are resolved
      if possible, or left unresolved otherwise.
    """
if '_tf_extension_type_cached_fields' in cls.__dict__:  # do not inherit.
    exit(cls._tf_extension_type_cached_fields)

try:
    # Using include_extras=False will replace all Annotated[T, ...] with T.
    # The typing_extensions module is used since this is only supported in
    # Python 3.9.
    type_hints = typing_extensions.get_type_hints(cls, include_extras=False)
    ok_to_cache = True  # all forward references have been resolved.
except (NameError, AttributeError):
    # Unresolved forward reference -- gather type hints manually.
    # * NameError comes from an annotation like `Foo` where class
    #   `Foo` hasn't been defined yet.
    # * AttributeError comes from an annotation like `foo.Bar`, where
    #   the module `foo` exists but `Bar` hasn't been defined yet.
    # Note: If a user attempts to instantiate a `ExtensionType` type that
    # still has unresolved forward references (e.g., because of a typo or a
    # missing import), then the constructor will raise an exception.
    type_hints = {}
    for base in reversed(cls.__mro__):
        type_hints.update(base.__dict__.get('__annotations__', {}))
    ok_to_cache = False

fields = []
for (name, value_type) in type_hints.items():
    default = getattr(cls, name,
                      extension_type_field.ExtensionTypeField.NO_DEFAULT)
    fields.append(
        extension_type_field.ExtensionTypeField(name, value_type, default))
fields = tuple(fields)

if ok_to_cache:
    cls._tf_extension_type_cached_fields = fields

exit(fields)
