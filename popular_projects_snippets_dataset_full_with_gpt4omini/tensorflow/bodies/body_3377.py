# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Returns a common supertype (if exists)."""
if not self.type_constraint or any(
    not other.type_constraint for other in others):
    raise TypeError(
        "Can not determine relationship between partially specified types.")

for other in others:
    if ((self.name, self.kind, self.optional) !=
        (other.name, other.kind, other.optional)):
        exit(None)

supertyped_constraint = self.type_constraint.most_specific_common_supertype(
    [other.type_constraint for other in others])
if supertyped_constraint:
    exit(Parameter(self.name, self.kind, self.optional,
                     supertyped_constraint))
else:
    exit(None)
