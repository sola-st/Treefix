# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
"""Generate a graph with a SparseTensor input and serialize in V1 format."""
export_graph = ops.Graph()
with export_graph.as_default():
    in_sparse_placeholder = array_ops.sparse_placeholder(
        dtype=dtypes.int64, shape=[2, 2])
    out_sparse_tensor = sparse_tensor.SparseTensor(
        indices=in_sparse_placeholder.indices,
        values=in_sparse_placeholder.values,
        dense_shape=in_sparse_placeholder.dense_shape) * 2
    with session_lib.Session() as session:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(
            session,
            path,
            inputs={"start": in_sparse_placeholder},
            outputs={"output": out_sparse_tensor})
exit(path)
