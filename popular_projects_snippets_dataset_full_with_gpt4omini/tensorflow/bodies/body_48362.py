# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
"""Assigns unique names to the Network's outputs.

    Output layers with multiple output tensors would otherwise lead to duplicate
    names in self.output_names.
    """
uniquified = []
output_names = set()
prefix_count = {}
for layer in self._output_layers:
    proposal = layer.name
    while proposal in output_names:
        existing_count = prefix_count.get(layer.name, 1)
        proposal = '{}_{}'.format(layer.name, existing_count)
        prefix_count[layer.name] = existing_count + 1
    output_names.add(proposal)
    uniquified.append(proposal)
self.output_names = uniquified
