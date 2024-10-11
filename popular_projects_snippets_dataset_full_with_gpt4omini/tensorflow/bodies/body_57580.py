# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TFLiteConverter class from a SavedModel.

    Args:
      saved_model_dir: SavedModel directory to convert.
      input_arrays: List of input tensors to freeze graph with. Uses input
        arrays from SignatureDef when none are provided. (default None)
      input_shapes: Dict of strings representing input tensor names to list of
        integers representing input shapes (e.g., {"foo" : [1, 16, 16, 3]}).
        Automatically determined when input shapes is None (e.g., {"foo" :
          None}). (default None)
      output_arrays: List of output tensors to freeze graph with. Uses output
        arrays from SignatureDef when none are provided. (default None)
      tag_set: Set of tags identifying the MetaGraphDef within the SavedModel to
        analyze. All tags in the tag set must be present. (default
        {tf.saved_model.SERVING})
      signature_key: Key identifying SignatureDef containing inputs and outputs.
        (default tf.saved_model.DEFAULT_SERVING_SIGNATURE_DEF_KEY)

    Returns:
      TFLiteConverter class.
    """
# pylint: disable=protected-access
TFLiteConverterBase._set_original_model_type(
    conversion_metdata_fb.ModelType.TF_SAVED_MODEL)
# pylint: enable=protected-access
if tag_set is None:
    tag_set = set([_tag_constants.SERVING])
if signature_key is None:
    signature_key = _signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY

saved_model_converter = TFLiteSavedModelConverter(saved_model_dir, tag_set,
                                                  [signature_key])
if saved_model_converter.saved_model_dir:
    exit(saved_model_converter)

result = _freeze_saved_model(saved_model_dir, input_arrays, input_shapes,
                             output_arrays, tag_set, signature_key)

exit(cls(
    graph_def=result[0],
    input_tensors=result[1],
    output_tensors=result[2],
    experimental_debug_info_func=_build_debug_info_func(result[3])))
