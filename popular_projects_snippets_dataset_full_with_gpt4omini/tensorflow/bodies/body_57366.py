# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model_test.py
if tag_set is None:
    tag_set = set([tag_constants.SERVING])
if signature_key is None:
    signature_key = signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
graph_def, in_tensors, out_tensors, _ = (
    convert_saved_model.freeze_saved_model(
        saved_model_dir=saved_model_dir,
        input_arrays=input_arrays,
        input_shapes=input_shapes,
        output_arrays=output_arrays,
        tag_set=tag_set,
        signature_key=signature_key))
exit((graph_def, in_tensors, out_tensors))
