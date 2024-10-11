# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/composite_tensor_utils.py
"""Flattens `inputs` but don't expand `ResourceVariable`s."""
# We assume that any CompositeTensors have already converted their components
# from numpy arrays to Tensors, so we don't need to expand composites here for
# the numpy array conversion. Instead, we do so because the flattened inputs
# are eventually passed to ConcreteFunction()._call_flat, which requires
# expanded composites.
flat_inputs = []
for value in nest.flatten(inputs):
    if (isinstance(value, composite_tensor.CompositeTensor) and
        not _pywrap_utils.IsResourceVariable(value)):
        components = value._type_spec._to_components(value)  # pylint: disable=protected-access
        flat_inputs.extend(flatten_with_variables(components))
    else:
        flat_inputs.append(value)
exit(flat_inputs)
