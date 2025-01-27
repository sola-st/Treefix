# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Converts one function argument into a constant.

    Args:
      incoming_edge: The edge into the argument to be converted.
      tensor_data: The constant value.
    """
index = incoming_edge.destination.index
for edge in self.outgoing_edges:
    if edge.source.index == index:
        edge.destination.convertible.convert_variable_to_constant(
            edge, tensor_data)

function = self.converted_self().function
function.signature.input_arg[index].type = tensor_data.dtype
# TODO(b/176982859): Find a more satisfying way to update shape information
# than clearing it, or migrate users to a workflow that does not require
# freezing.
if "_input_shapes" in function.attr:
    function.attr["_input_shapes"].list.shape[index].unknown_rank = True
    del function.attr["_input_shapes"].list.shape[index].dim[:]
arg_attrs = function.arg_attr[index].attr
if "_output_shapes" in arg_attrs:
    arg_attrs["_output_shapes"].list.shape[0].unknown_rank = True
    del arg_attrs["_output_shapes"].list.shape[0].dim[:]
