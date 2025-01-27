# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Computes output tensors for new inputs.

    # Note:
        - Can be run on non-Keras tensors.

    Args:
        inputs: Tensor or nested structure of Tensors.
        training: Boolean learning phase.
        mask: (Optional) Tensor or nested structure of Tensors.

    Returns:
        output_tensors
    """
inputs = self._flatten_to_reference_inputs(inputs)
if mask is None:
    masks = [None] * len(inputs)
else:
    masks = self._flatten_to_reference_inputs(mask)
for input_t, mask in zip(inputs, masks):
    input_t._keras_mask = mask

# Dictionary mapping reference tensors to computed tensors.
tensor_dict = {}
tensor_usage_count = self._tensor_usage_count
for x, y in zip(self.inputs, inputs):
    y = self._conform_to_reference_input(y, ref_input=x)
    x_id = str(id(x))
    tensor_dict[x_id] = [y] * tensor_usage_count[x_id]

nodes_by_depth = self._nodes_by_depth
depth_keys = list(nodes_by_depth.keys())
depth_keys.sort(reverse=True)

for depth in depth_keys:
    nodes = nodes_by_depth[depth]
    for node in nodes:
        if node.is_input:
            continue  # Input tensors already exist.

        if any(t_id not in tensor_dict for t_id in node.flat_input_ids):
            continue  # Node is not computable, try skipping.

        args, kwargs = node.map_arguments(tensor_dict)
        outputs = node.layer(*args, **kwargs)

        # Update tensor_dict.
        for x_id, y in zip(node.flat_output_ids, nest.flatten(outputs)):
            tensor_dict[x_id] = [y] * tensor_usage_count[x_id]

output_tensors = []
for x in self.outputs:
    x_id = str(id(x))
    assert x_id in tensor_dict, 'Could not compute output ' + str(x)
    output_tensors.append(tensor_dict[x_id].pop())

exit(nest.pack_sequence_as(self._nested_outputs, output_tensors))
