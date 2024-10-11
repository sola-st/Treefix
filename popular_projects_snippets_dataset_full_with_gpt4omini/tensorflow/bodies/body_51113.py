# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(
    lambda x: math_ops.mul(2., x, name="DEBUG_INFO_OP"),
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
save_dir = os.path.join(self.get_temp_dir(), "saved_model")
save.save(
    root,
    save_dir,
    root.f,
    options=save_options.SaveOptions(save_debug_info=True))
debug_info_file_name = os.path.join(save_dir, "debug",
                                    "saved_model_debug_info.pb")
self.assertTrue(os.path.exists(debug_info_file_name))
debug_info = graph_debug_info_pb2.GraphDebugInfo()
with open(debug_info_file_name, "rb") as f:
    debug_info.ParseFromString(f.read())

# Verify that there is a trace for DEBUG_INFO_OP just to ensure that
# function debug info tracing is nominally functioning.
found_op = False
for key in debug_info.traces.keys():
    if key.startswith("DEBUG_INFO_OP@"):
        found_op = True
        break
self.assertTrue(found_op, "Did not find DEBUG_INFO_OP in trace")
