# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""This adds the nodes to out_graphdef and returns an aggregated output.

    In particular, if you have 4 inputs to a hint stub, this will be the
    node that you can use as an output. I.e. you have 4 timesteps from a
    static rnn, then a fused UnidirectionalLSTM will expect 1 input with
    all 4 time steps. So here we make a pack and return the output name of
    that pack.

    Args:
      out_graphdef: A graphdef that is ready to have this input added.

    Returns:
      The name of a pack that aggregates this node.
    """
flattened = self.flatten_nodes()
if (self.aggregation == OpHint.AGGREGATE_FIRST) or (
    self.aggregation == OpHint.AGGREGATE_LAST):
    assert len(flattened) == 1
if len(flattened) == 1 and self.aggregation != OpHint.AGGREGATE_STACK:
    exit(_tensor_name_base(flattened[0].name))
else:
    new_node = _node_def_pb2.NodeDef()
    new_node.op = "Pack"
    new_node.name = "OpHintStack-%s" % flattened[0].name
    new_node.attr["N"].i = len(flattened)
    new_node.attr["T"].type = flattened[0].attr["T"].type
    for discrete in flattened:
        new_node.input.append(_tensor_name_base(discrete.name))
    out_graphdef.node.extend([new_node])
    exit(new_node.name)
