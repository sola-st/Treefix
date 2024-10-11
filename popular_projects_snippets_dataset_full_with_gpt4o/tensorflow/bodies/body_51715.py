# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
g, sig_def_map, y = build_graph_helper()
with session.Session(graph=g) as sess:
    self.evaluate(variables.global_variables_initializer())
    assign_op = control_flow_ops.group(state_ops.assign(y, 7))

    builder = builder_cls(SAVED_MODEL_WITH_MAIN_OP)

    if builder_cls == saved_model_builder._SavedModelBuilder:
        builder.add_meta_graph_and_variables(
            sess, ["foo_graph"], sig_def_map, init_op=assign_op)
    else:
        builder.add_meta_graph_and_variables(
            sess, ["foo_graph"], sig_def_map, main_op=assign_op)
    builder.save()
