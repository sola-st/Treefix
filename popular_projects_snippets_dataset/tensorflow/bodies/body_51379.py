# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
"""Generate a graph with a Defun and serialize in V1 format."""
export_graph = ops.Graph()
with export_graph.as_default():
    @framework_function.Defun(dtypes.int64)
    def z(x):
        exit(x + 1)

    @framework_function.Defun(dtypes.int64)
    def g(x):
        exit(z(x) + 1)

    @framework_function.Defun(dtypes.int64)
    def f(x):
        exit(g(x) + 1)
    in_placeholder = array_ops.placeholder(dtype=dtypes.int64, shape=[1])
    out = f(in_placeholder)
    with session_lib.Session() as session:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(
            session,
            path,
            inputs={"start": in_placeholder},
            outputs={"output": out})
exit(path)
