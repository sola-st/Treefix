# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Compute the #. of tensor usages for all the output tensors of layers.

    The computed tensor usage count is saved as `self._tensor_usage_count`. This
    is later used for saving memory in eager computation by releasing
    no-longer-needed tensors as early as possible.
    """
tensor_usage_count = collections.Counter()
available_tensors = set(str(id(tensor)) for tensor in self.inputs)

depth_keys = list(self._nodes_by_depth.keys())
depth_keys.sort(reverse=True)
depth_keys = depth_keys[1:]

for depth in depth_keys:
    for node in self._nodes_by_depth[depth]:
        input_tensors = {
            str(id(tensor)) for tensor in nest.flatten(node.keras_inputs)
        }
        if input_tensors.issubset(available_tensors):
            for tensor in nest.flatten(node.keras_inputs):
                tensor_usage_count[str(id(tensor))] += 1

            for output_tensor in nest.flatten(node.outputs):
                available_tensors.add(str(id(output_tensor)))

for tensor in self.outputs:
    tensor_usage_count[str(id(tensor))] += 1

self._tensor_usage_count = tensor_usage_count
