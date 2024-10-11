# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_util.py
graph = graph or ops.get_default_graph()
global_step_tensor = get_global_step(graph)
if global_step_tensor is None:
    raise ValueError(
        'Global step tensor should be created by '
        'tf.train.get_or_create_global_step before calling increment.')
global_step_read_tensor = _get_or_create_global_step_read(graph)
with graph.as_default() as g, g.name_scope(None):
    with g.name_scope(global_step_tensor.op.name + '/'):
        with ops.control_dependencies([global_step_read_tensor]):
            exit(state_ops.assign_add(global_step_tensor, increment))
