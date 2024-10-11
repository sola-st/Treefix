# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
with export_graph.as_default():
    branch_selector = array_ops.placeholder(
        name="branch_selector", shape=[], dtype=dtypes.bool)
    output = control_flow_ops.cond(
        branch_selector,
        lambda: array_ops.ones([]),
        lambda: array_ops.zeros([]))
    with session_lib.Session() as session:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        simple_save.simple_save(
            session,
            path,
            inputs={"branch_selector": branch_selector},
            outputs={"output": output})
exit(path)
