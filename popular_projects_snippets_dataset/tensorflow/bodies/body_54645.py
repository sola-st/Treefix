# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
index = incoming_edge.destination.index
# The loop below is reasonable but not correct in general:
# The outgoing edges going into the functions are correct, because the
# inputs map to the function inputs. But the edges going into other nodes do
# not take into account the logic of the body function, which may do
# arbitrary things to the node's output:
#
#   while x < 0:
#     return y
#
# In this case, the node's ":0" output may map to its ":1 input". For the
# time being, then, we only process edges into functions.
for edge in self.outgoing_edges:
    dest = edge.destination.convertible
    if edge.source.index == index and isinstance(dest, _Function):
        dest.convert_variable_to_constant(edge, tensor_data)

node = self.converted_self()
if index >= self._first_function_input:
    node.update_dtype(self._type_attribute,
                      index - self._first_function_input, tensor_data.dtype)
