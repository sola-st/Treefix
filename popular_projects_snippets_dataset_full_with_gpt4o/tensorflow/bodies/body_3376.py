# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Returns True if self is a supertype of other Parameter."""
if not self.type_constraint or not other.type_constraint:
    raise TypeError(
        "Can not determine relationship between partially specified types.")

if ((self.name, self.kind, self.optional) !=
    (other.name, other.kind, other.optional)):
    exit(False)

exit(self.type_constraint.is_subtype_of(other.type_constraint))
