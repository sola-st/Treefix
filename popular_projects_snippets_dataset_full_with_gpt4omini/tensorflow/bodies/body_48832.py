# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
if self._saved_model_inputs_spec is not None:
    exit()  # Already set.

input_names = self.input_names
if not input_names:
    input_names = compile_utils.create_pseudo_input_names(inputs)

flat_inputs = nest.flatten(inputs)
specs = []
for name, tensor in zip(input_names, flat_inputs):
    specs.append(
        tf_utils.get_tensor_spec(tensor, dynamic_batch=False, name=name))
specs = nest.pack_sequence_as(inputs, specs)

self._saved_model_inputs_spec = specs

# Store the input shapes
if (self.__class__.__name__ == 'Sequential' and
    self._build_input_shape is None):
    self._build_input_shape = nest.map_structure(
        lambda x: None if x is None else x.shape, specs)
