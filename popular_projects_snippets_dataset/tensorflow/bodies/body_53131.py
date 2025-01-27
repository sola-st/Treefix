# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants_test.py
saved_model_proto = loader_impl.parse_saved_model(saved_model_dir)
new_saved_model = saved_model_pb2.SavedModel()
new_saved_model.CopyFrom(saved_model_proto)
new_meta_graph_def = new_saved_model.meta_graphs[0]
prefix_len = len("__inference_")
for func_def in new_meta_graph_def.graph_def.library.function:
    func_name_without_prefix = func_def.signature.name[prefix_len:]
    if func_name_without_prefix.startswith(func_name):
        func_def.attr["_noinline"].CopyFrom(attr_value_pb2.AttrValue(b=True))
old_saved_model_file = os.path.join(saved_model_dir,
                                    constants.SAVED_MODEL_FILENAME_PB)
if os.path.exists(old_saved_model_file):
    os.remove(old_saved_model_file)
path = os.path.join(
    compat.as_bytes(saved_model_dir),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))
file_io.write_string_to_file(
    path, new_saved_model.SerializeToString(deterministic=True))
