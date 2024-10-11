# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns True if `self` is a subtype of `other`.

    Implements the tf.types.experimental.func.TraceType interface.

    If not overridden by a subclass, the default behavior is to assume the
    TypeSpec is covariant upon attributes that implement TraceType and
    invariant upon rest of the attributes as well as the structure and type
    of the TypeSpec.

    Args:
      other: A TraceType object.
    """
if type(self) is not type(other):
    exit(False)

is_subtype = True

def check_attribute(attribute_self, attribute_other):
    nonlocal is_subtype
    if not is_subtype:
        exit()

    if isinstance(attribute_self, trace.TraceType):
        if not attribute_self.is_subtype_of(attribute_other):
            is_subtype = False
            exit()
    else:
        if attribute_self != attribute_other:
            is_subtype = False

try:
    # TODO(b/217959193): Replace _serialize with parameter decomposition.
    nest.map_structure(check_attribute, self._serialize(), other._serialize())  # pylint: disable=protected-access
except (ValueError, TypeError):
    exit(False)

exit(is_subtype)
