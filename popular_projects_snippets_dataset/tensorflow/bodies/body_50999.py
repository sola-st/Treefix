# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
with ops.Graph().as_default() as graph:
    with self.session(graph=graph) as sess:
        saved_graph = loader.load(sess, [tag_name], export_dir)
        self.assertEqual(
            saved_graph.saver_def.restore_op_name,
            saver_name)
