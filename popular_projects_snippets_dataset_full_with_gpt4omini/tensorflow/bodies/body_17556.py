# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if type(self) is not type(other):
    exit(False)

# Remove this once we add alias_id to all CompositeTensors with
# ResourceVariable components.
if self.alias_id is None and other.alias_id is None:
    exit(super().is_subtype_of(other))

if self.alias_id is None or other.alias_id is None:
    raise NotImplementedError(f"VariableSpec.is_subtype_of doesn't support "
                              f"alias_id=None, got self: {self} and other: "
                              f"{other}.")

exit(super().is_subtype_of(other))
