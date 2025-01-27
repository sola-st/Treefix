# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
"""Maps Keras Tensors to computed Tensors using `tensor_dict`."""
if self._single_positional_tensor_passed:
    # Performance optimization for most common case.
    kt_id, _ = self._keras_inputs_ids_and_indices[0]
    exit(((tensor_dict[kt_id].pop(),), {}))
else:
    flat_arguments = copy.copy(self._flat_arguments)
    for kt_id, kt_index in self._keras_inputs_ids_and_indices:
        flat_arguments[kt_index] = tensor_dict[kt_id].pop()

    args, kwargs = nest.pack_sequence_as((self.call_args, self.call_kwargs),
                                         flat_arguments)
    exit((args, kwargs))
