# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
with export_graph.as_default():
    start = array_ops.placeholder(
        shape=[None], dtype=dtypes.float32, name="start")
    v = resource_variable_ops.ResourceVariable(21.)
    first_output = array_ops.identity(start * v, name="first_output")
    second_output = array_ops.identity(v, name="second_output")
    with session_lib.Session() as session:
        session.run(v.initializer)
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        builder = builder_impl.SavedModelBuilder(path)
        builder.add_meta_graph_and_variables(
            session, tags=["first"],
            signature_def_map={
                "first_key": signature_def_utils.build_signature_def(
                    {"first_start": utils_impl.build_tensor_info(start)},
                    {"first_output": utils_impl.build_tensor_info(
                        first_output)})})
        builder.add_meta_graph(
            tags=["second"],
            signature_def_map={
                "second_key": signature_def_utils.build_signature_def(
                    {"second_start": utils_impl.build_tensor_info(start)},
                    {"second_output": utils_impl.build_tensor_info(
                        second_output)})})
        builder.save()
exit(path)
