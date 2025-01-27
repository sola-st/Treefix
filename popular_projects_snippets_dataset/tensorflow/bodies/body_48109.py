# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
self._inputs = inputs
self._is_dict = isinstance(self._inputs, dict)
self._is_single_input = not isinstance(self._inputs, (list, tuple, dict))

self._flattened_inputs = []
self._input_names = []

if self._is_dict:
    for k in sorted(self._inputs.keys()):
        self._flattened_inputs.append(self._inputs[k])
        self._input_names.append(k)
else:
    self._flattened_inputs = nest.flatten(self._inputs)
    self._input_names = [
        'input_%d' % (i + 1) for i in range(len(self._flattened_inputs))
    ]
