# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
"""Test saved model with multiple MetaGraphDefs."""
saved_model_dir = os.path.join(self.get_temp_dir(), "savedmodel_two_mgd")
builder = saved_model.builder.SavedModelBuilder(saved_model_dir)
with session.Session(graph=ops.Graph()) as sess:
    # MetaGraphDef 1
    in_tensor = array_ops.placeholder(shape=[1, 28, 28], dtype=dtypes.float32)
    out_tensor = in_tensor + in_tensor
    sig_input_tensor = saved_model.utils.build_tensor_info(in_tensor)
    sig_input_tensor_signature = {"x": sig_input_tensor}
    sig_output_tensor = saved_model.utils.build_tensor_info(out_tensor)
    sig_output_tensor_signature = {"y": sig_output_tensor}
    predict_signature_def = (
        saved_model.signature_def_utils.build_signature_def(
            sig_input_tensor_signature, sig_output_tensor_signature,
            saved_model.signature_constants.PREDICT_METHOD_NAME))
    signature_def_map = {
        saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
            predict_signature_def
    }
    builder.add_meta_graph_and_variables(
        sess,
        tags=[saved_model.tag_constants.SERVING, "additional_test_tag"],
        signature_def_map=signature_def_map)

    # MetaGraphDef 2
    builder.add_meta_graph(tags=["tflite"])
    builder.save(True)

# Convert to tflite
_, in_tensors, out_tensors = self._convertSavedModel(
    saved_model_dir=saved_model_dir,
    tag_set=set([saved_model.tag_constants.SERVING, "additional_test_tag"]))

self.assertEqual(self._getArrayNames(out_tensors), ["add:0"])
self.assertEqual(self._getArrayNames(in_tensors), ["Placeholder:0"])
self.assertEqual(self._getArrayShapes(in_tensors), [[1, 28, 28]])
