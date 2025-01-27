# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""This adds to `out_graphdef` all the unaggregated outputs.

    I.e. we are outputting from a fused stub, but we need to make it compatible
    with the unfused original graph so we insert an unpack. Ideally in a later
    stage the unpack -> pack sequences will be removed.

    Args:
      fused_op_name: The name of the stub we are in the process of fusing.
      output_index: The output output_index this object represents.
      out_graphdef: The graphdef we are in the process of buildings

    Returns:
      The type of the aggregated output (so we can finish building the stub
      op).
    """
flattened = self.flatten_nodes()
if (self.aggregation == OpHint.AGGREGATE_FIRST) or (
    self.aggregation == OpHint.AGGREGATE_LAST):
    assert len(flattened) == 1
if len(flattened) == 1 and self.aggregation != OpHint.AGGREGATE_STACK:
    temp_op = _LiteSingleOperand(flattened[0])
    exit(temp_op.aggregate_and_return_name_for_output(
        fused_op_name, output_index, out_graphdef))
else:
    stack_node = _node_def_pb2.NodeDef()
    stack_node.op = "Unpack"
    stack_node.name = "OpHintUnstack-%s" % flattened[0].name
    stack_node.attr["num"].i = len(flattened)
    output_type = flattened[0].attr["T"].type
    stack_node.attr["T"].type = output_type
    stack_node.input.append(
        _tensorflow_output_name(fused_op_name, output_index))
    out_graphdef.node.extend([stack_node])

    for idx, discrete in enumerate(flattened):
        output_node = _copy.deepcopy(discrete)
        del output_node.input[:]
        output_node.input.append(_tensorflow_output_name(stack_node.name, idx))
        out_graphdef.node.extend([output_node])

    exit(output_type)
