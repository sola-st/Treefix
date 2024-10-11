# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_function_test.py
"""Write the saved model as an input for testing.

    In addition to creating a SavedModel like its parent method, this method
    replaces this SavedModel by adding TF-TRT conversion parameters as function
    attributes to each function in the SavedModel.

    Args:
      run_params: The current test run parameters.

    Returns:
      The directory of the saved model.
    """
saved_model_dir = trt_test.TfTrtIntegrationTestBase._MakeSavedModelV1(
    self, run_params)
saved_model_proto = loader_impl.parse_saved_model(saved_model_dir)
new_saved_model = saved_model_pb2.SavedModel()
new_saved_model.CopyFrom(saved_model_proto)
new_meta_graph_def = new_saved_model.meta_graphs[0]
for func_def in new_meta_graph_def.graph_def.library.function:
    # Disable function inlining.
    func_def.attr["_noinline"].CopyFrom(attr_value_pb2.AttrValue(b=True))
    self._copy_test_attributes_to_func_def(func_def)
old_saved_model_file = os.path.join(saved_model_dir,
                                    constants.SAVED_MODEL_FILENAME_PB)
if os.path.exists(old_saved_model_file):
    os.remove(old_saved_model_file)
path = os.path.join(
    compat.as_bytes(saved_model_dir),
    compat.as_bytes(constants.SAVED_MODEL_FILENAME_PB))
file_io.write_string_to_file(
    path, new_saved_model.SerializeToString(deterministic=True))
exit(saved_model_dir)
