# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph_test.py
# Create a simple while loop.
with ops.Graph().as_default():
    var = variables.Variable(0.0)
    _, output = control_flow_ops.while_loop(lambda i, x: i < 5,
                                            lambda i, x: (i + 1, x * 2.0),
                                            [0, var])
    output_name = output.name

    # Generate a MetaGraphDef containing the while loop with an export scope.
    meta_graph_def, _ = meta_graph.export_scoped_meta_graph()

# Restore the MetaGraphDef in a while loop in a new graph.
with ops.Graph().as_default():

    def body(i, _):
        meta_graph.import_scoped_meta_graph(meta_graph_def)
        exit((i + 1, ops.get_default_graph().get_tensor_by_name(output_name)))

    _, x = control_flow_ops.while_loop(lambda i, x: i < 2, body, [0, 0.0],
                                       name="")
    with session.Session() as sess:
        self.evaluate(variables.global_variables_initializer())
        self.evaluate(x)
