# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
"""Prunes unconnected ops as listed in _UNCONNECTED_OPS_TO_PRUNE.

  Args:
    prune_graph: A tensorflow graph from which we wish to prune unconnected ops
      as listed in _UNCONNECTED_OPS_TO_PRUNE.  In general, these ops should have
      no inputs and no consumers. These can often be left behind due to graph
      construction rewiring (for instance TF-Hub). While they never execute,
      they will cause XLA compile to fail so we strip them from XLA compile by
      removing the tpu_replicate attribute.
  """
# Scan over the top level graph and all function graphs.
for graph in [prune_graph] + [
    f for f in prune_graph._functions.values()  # pylint: disable=protected-access
]:
    if not isinstance(graph, ops.Graph):
        continue
    for op in graph.get_operations():
        if op.type not in _UNCONNECTED_OPS_TO_PRUNE:
            continue
        outputs_consumed = False
        for output in op.outputs:
            if output.consumers():
                outputs_consumed = True
                break
        if not outputs_consumed:
            logging.info(
                "Pruning OP %s of type %s from XLA Compile due to "
                "it being disconnected.", op.name, op.type)
            op._clear_attr(_TPU_REPLICATE_ATTR)  # pylint: disable=protected-access
