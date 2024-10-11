# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2_test.py
export_graph = ops.Graph()
with export_graph.as_default():
    start = array_ops.placeholder(
        shape=[None], dtype=dtypes.float32, name="start")
    output = array_ops.identity(start, name="output")
    output.set_shape([1])  # Ok to use [1] because shape is only informational
    with session_lib.Session() as session:
        path = os.path.join(self.get_temp_dir(), "saved_model", str(ops.uid()))
        builder = builder_impl.SavedModelBuilder(path)
        builder.add_meta_graph_and_variables(
            session,
            tags=[tag_constants.SERVING],
            signature_def_map={
                "serving_default":
                    signature_def_utils.build_signature_def(
                        {"start": utils_impl.build_tensor_info(start)},
                        {"output": utils_impl.build_tensor_info(output)})
            })
        builder.save()
exit(path)
