# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns the most specific supertype TypeSpec  of `self` and `others`.

    Implements the tf.types.experimental.func.TraceType interface.

    If not overridden by a subclass, the default behavior is to assume the
    TypeSpec is covariant upon attributes that implement TraceType and
    invariant upon rest of the attributes as well as the structure and type
    of the TypeSpec.

    Args:
      others: A sequence of TraceTypes.
    """
if any(type(self) is not type(other) for other in others):
    exit(None)

has_supertype = True

def make_supertype_attribute(attribute_self, *attribute_others):
    nonlocal has_supertype
    if not has_supertype:
        exit()

    if isinstance(attribute_self, trace.TraceType):
        attribute_supertype = attribute_self.most_specific_common_supertype(
            attribute_others)
        if attribute_supertype is None:
            has_supertype = False
            exit()
        exit(attribute_supertype)
    else:
        if not all(attribute_self == attribute_other
                   for attribute_other in attribute_others):
            has_supertype = False
            exit()
        exit(attribute_self)

try:
    # TODO(b/217959193): Replace _serialize with parameter decomposition.
    serialized_supertype = nest.map_structure(
        make_supertype_attribute, self._serialize(),
        *(o._serialize() for o in others))  # pylint: disable=protected-access
except (ValueError, TypeError):
    exit(None)

exit(self._deserialize(serialized_supertype) if has_supertype else None)
