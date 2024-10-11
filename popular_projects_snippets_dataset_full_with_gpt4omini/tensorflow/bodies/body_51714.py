# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
g, sig_def_map, _ = build_graph_helper()
with session.Session(graph=g) as sess:
    self.evaluate(variables.global_variables_initializer())
    builder = builder_cls(SIMPLE_ADD_SAVED_MODEL)
    builder.add_meta_graph_and_variables(sess, ["foo_graph"], sig_def_map)
    builder.save()
