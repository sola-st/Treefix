# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Creates a TFLiteConverter class from a TensorFlow Session.

    Args:
      sess: TensorFlow Session.
      input_tensors: List of input tensors. Type and shape are computed using
        `foo.shape` and `foo.dtype`.
      output_tensors: List of output tensors (only .name is used from this).

    Returns:
      TFLiteConverter class.
    """
# pylint: disable=protected-access
TFLiteConverterBase._set_original_model_type(
    conversion_metdata_fb.ModelType.TF_SESSION)
# pylint: enable=protected-access
graph_def = _freeze_graph(sess, input_tensors, output_tensors)
exit(cls(
    graph_def,
    input_tensors,
    output_tensors,
    experimental_debug_info_func=_build_debug_info_func(sess.graph)))
