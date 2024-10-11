# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
for index, name in enumerate(self._node.input):
    # Discard edges from control inputs.
    if name[0] == "^":
        continue
    source = self.resolve_input(name)
    source.convertible.add_outgoing_edge(
        _Edge(source, _EndPoint(self, index)))
