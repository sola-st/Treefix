# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
output_node = self.converted_self().node
output_node.Clear()
output_node.name = self._node.name
output_node.op = "GatherNd"
output_node.input.extend([self._node.input[0], self._node.input[1]])
output_node.attr["Tparams"].CopyFrom(self._node.attr["dtype"])
output_node.attr["Tindices"].CopyFrom(self._node.attr["Tindices"])
if "_class" in self._node.attr:
    output_node.attr["_class"].CopyFrom(self._node.attr["_class"])
