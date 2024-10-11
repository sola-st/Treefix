# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
with export_graph.as_default():
    input1 = array_ops.placeholder(
        shape=[None], dtype=dtypes.float32, name="input1")
    input2 = array_ops.placeholder(
        shape=[None], dtype=dtypes.float32, name="input2")
    v = resource_variable_ops.ResourceVariable(21.)
    output = array_ops.identity(input1 * v + input2, name="output")
    with session_lib.Session() as session:
        session.run(v.initializer)
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        builder = builder_impl.SavedModelBuilder(path)
        builder.add_meta_graph_and_variables(
            session,
            tags=[tag_constants.SERVING],
            signature_def_map={
                "serving_default":
                    signature_def_utils.build_signature_def(
                        {
                            "input1": utils_impl.build_tensor_info(input1),
                            "input2": utils_impl.build_tensor_info(input2)
                        }, {"output": utils_impl.build_tensor_info(output)})
            })
        builder.save()
exit(path)
