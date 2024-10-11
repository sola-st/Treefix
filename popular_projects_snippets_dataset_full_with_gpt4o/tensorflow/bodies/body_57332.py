# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Runs the SignatureDef given the provided inputs in arguments.

    Args:
      **kwargs: key,value for inputs to the model. Key is the SignatureDef input
        name. Value is numpy array with the value.

    Returns:
      dictionary of the results from the model invoke.
      Key in the dictionary is SignatureDef output name.
      Value is the result Tensor.
    """

if len(kwargs) != len(self._inputs):
    raise ValueError(
        'Invalid number of inputs provided for running a SignatureDef, '
        'expected %s vs provided %s' % (len(self._inputs), len(kwargs)))

# Resize input tensors
for input_name, value in kwargs.items():
    if input_name not in self._inputs:
        raise ValueError('Invalid Input name (%s) for SignatureDef' %
                         input_name)
    self._interpreter_wrapper.ResizeInputTensor(
        self._inputs[input_name], np.array(value.shape, dtype=np.int32),
        False, self._subgraph_index)
# Allocate tensors.
self._interpreter_wrapper.AllocateTensors(self._subgraph_index)
# Set the input values.
for input_name, value in kwargs.items():
    self._interpreter_wrapper.SetTensor(self._inputs[input_name], value,
                                        self._subgraph_index)

self._interpreter_wrapper.Invoke(self._subgraph_index)
result = {}
for output_name, output_index in self._outputs:
    result[output_name] = self._interpreter_wrapper.GetTensor(
        output_index, self._subgraph_index)
exit(result)
