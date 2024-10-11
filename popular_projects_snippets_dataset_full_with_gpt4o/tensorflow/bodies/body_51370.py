# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
"""Generate a graph with a SparseTensor output and serialize in V1 format"""
export_graph = ops.Graph()
with export_graph.as_default():
    in_placeholder = array_ops.placeholder(dtype=dtypes.int64, shape=[1])
    out_sparse_tensor = sparse_tensor.SparseTensor(
        indices=[[0]], values=in_placeholder, dense_shape=[1]) * 2
    with session_lib.Session() as session:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(
            session,
            path,
            inputs={"start": in_placeholder},
            outputs={"output": out_sparse_tensor})
exit(path)
