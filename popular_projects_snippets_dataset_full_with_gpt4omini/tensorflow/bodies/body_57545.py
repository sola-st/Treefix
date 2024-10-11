# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Convert the given ConcreteFunction to frozen graph.

    Returns:
      graph_def: The frozen GraphDef.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.
      frozen_func: The frozen ConcreteFunction.

    Raises:
      ValueError: none or multiple ConcreteFunctions provided.
    """
# TODO(b/130297984): Add support for converting multiple function.

if len(self._funcs) == 0:  # pylint: disable=g-explicit-length-test
    raise ValueError("No ConcreteFunction is specified.")

if len(self._funcs) > 1:
    raise ValueError("This converter can only convert a single "
                     "ConcreteFunction. Converting multiple functions is "
                     "under development.")

frozen_func, graph_def = (
    _convert_to_constants.convert_variables_to_constants_v2_as_graph(
        self._funcs[0], lower_control_flow=False))

input_tensors = [
    tensor for tensor in frozen_func.inputs
    if tensor.dtype != _dtypes.resource
]
output_tensors = frozen_func.outputs
exit((graph_def, input_tensors, output_tensors, frozen_func))
