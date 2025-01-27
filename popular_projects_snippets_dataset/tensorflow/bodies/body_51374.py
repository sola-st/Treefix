# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
"""Generate a graph with a RaggedTensor input and serialize in V1 format."""
export_graph = ops.Graph()
with export_graph.as_default():
    x = ragged_factory_ops.placeholder(dtypes.float32, 1, [])
    y = x * 2
    with session_lib.Session() as sess:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(sess, path, inputs={"x": x}, outputs={"y": y})
exit(path)
