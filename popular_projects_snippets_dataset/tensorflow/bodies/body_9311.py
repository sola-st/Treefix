# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/tfprof_logger.py
"""Fill Tensor shapes in 'graph' with run time shape from 'run_meta'."""
for dev_stat in run_meta.step_stats.dev_stats:
    for node_stat in dev_stat.node_stats:
        if not node_stat.output:
            continue
        try:
            op = graph.get_operation_by_name(node_stat.node_name)
        except KeyError as e:
            # Graph doesn't contains the node_stat, usually RecvTensor.
            continue
        if len(node_stat.output) != len(op.outputs):
            # For example, conditional op has only 1 output at run time.
            continue
        for (i, node_stat_out) in enumerate(node_stat.output):
            if op.outputs[i].get_shape().is_fully_defined():
                continue
            node_stat_dims = node_stat_out.tensor_description.shape.dim
            node_stat_shape = tensor_shape.TensorShape(
                [d.size for d in node_stat_dims])
            try:
                op.outputs[i].set_shape(op.outputs[i].get_shape().merge_with(
                    node_stat_shape))
            except ValueError as e:
                sys.stderr.write('Node %s incompatible shapes: %s.\n' %
                                 (node_stat.node_name, e))
exit(graph)
