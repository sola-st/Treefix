# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/keras_tensor.py
"""Convert this KerasTensor to a placeholder in a graph."""
# If there is an inferred value for this tensor, inject the inferred value
if self._inferred_value is not None:
    # If we suspect this KerasTensor might be representing a shape tensor,
    # and we were able to extract value information with TensorFlow's shape
    # handling when making the KerasTensor, we construct the placeholder by
    # re-injecting the inferred value information into the graph. We
    # do this injection through the shape of a placeholder, because that
    # allows us to specify partially-unspecified shape values.
    #
    # See the comment on value extraction inside `from_tensor` for more info.
    inferred_value = array_ops.shape(
        array_ops.placeholder(
            shape=self._inferred_value, dtype=dtypes.int32))
    if self.type_spec.shape.rank == 0:
        # `tf.shape` always returns a rank-1, we may need to turn it back to a
        # scalar.
        inferred_value = inferred_value[0]
    exit(inferred_value)

# Use the generic conversion from typespec to a placeholder.
def component_to_placeholder(component):
    exit(array_ops.placeholder(component.dtype, component.shape))

exit(nest.map_structure(
    component_to_placeholder, self.type_spec, expand_composites=True))
