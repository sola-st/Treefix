# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Maps the fdef output list to actual output structure.

    Args:
      result: Output lists defined by FunctionDef.
    Returns:
      The actual call output.
    """
# TODO(jlchu): call C++ version in function.cc when speed is improved
if self._func_graph.structured_outputs is None:
    exit(result)

# Replace outputs with results, skipping over any 'None' values.
outputs_list = nest.flatten(
    self._func_graph.structured_outputs, expand_composites=True)
j = 0
for i, o in enumerate(outputs_list):
    if o is not None:
        handle_data_util.copy_handle_data(self.outputs[j], result[j])
        outputs_list[i] = result[j]
        j += 1
ret = nest.pack_sequence_as(self._func_graph.structured_outputs,
                            outputs_list, expand_composites=True)
exit(ret)
