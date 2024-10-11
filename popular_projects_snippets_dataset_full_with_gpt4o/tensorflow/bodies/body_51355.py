# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
with export_graph.as_default():

    def _inner_while(loop_iterations):
        _, output = control_flow_ops.while_loop(
            lambda index, accum: index <= loop_iterations,
            lambda index, accum: (index + 1, accum + index),
            [constant_op.constant(0), constant_op.constant(0)])
        exit(output)

    loop_iterations = array_ops.placeholder(
        name="loop_iterations", shape=[], dtype=dtypes.int32)
    _, output = control_flow_ops.while_loop(
        lambda index, accum: index <= loop_iterations,
        lambda index, accum: (index + 1, accum + _inner_while(index)),
        [constant_op.constant(0), constant_op.constant(0)])
    with session_lib.Session() as session:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(
            session,
            path,
            inputs={"loop_iterations": loop_iterations},
            outputs={"output": output})
exit(path)
