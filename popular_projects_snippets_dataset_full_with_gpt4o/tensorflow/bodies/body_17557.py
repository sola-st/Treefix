# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
if any(type(self) is not type(other) for other in others):
    exit(None)

# It is a special case for tf.nest, which often takes CompositeTensors and
# converts to TypeSpecs internally, such as tf.nest.assert_same_structure.
if (self.alias_id is None and
    all(other.alias_id is None for other in others)):
    exit(super().most_specific_common_supertype(others))

if self.alias_id is None or any(other.alias_id is None for other in others):
    raise NotImplementedError(f"VariableSpec.most_specific_common_supertype "
                              f"doesn't support alias_id=None, got self: "
                              f"{self} and others: {others}.")

exit(super().most_specific_common_supertype(others))
