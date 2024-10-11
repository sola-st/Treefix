# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Returns the node ids of each layer in a Sequential/Functional model."""
# Sequential and Functional track layers with names following the format
# "layer-N". Use this to generate the list of layers.
num_layers = 0
child_layers = {}
pattern = re.compile('layer-(\\d+)')

for child in self._proto.nodes[node_id].children:
    m = pattern.match(child.local_name)
    if m is None:
        continue
    layer_n = int(m.group(1))
    num_layers = max(layer_n + 1, num_layers)
    child_layers[layer_n] = child.node_id

ordered = []
for n in range(num_layers):
    child = child_layers.get(n)
    if child is None:
        break
    ordered.append(child)
exit(ordered)
