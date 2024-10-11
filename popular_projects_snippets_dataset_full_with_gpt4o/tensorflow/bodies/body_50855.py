# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/metrics_test.py
save_dir = os.path.join(self.get_temp_dir(), "builder")
builder_ = builder.SavedModelBuilder(save_dir)

with ops.Graph().as_default():
    with self.session(graph=ops.Graph()) as sess:
        constant_op.constant(5.0)
        builder_.add_meta_graph_and_variables(sess, ["foo"])
    builder_.save()
exit(save_dir)
