# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Constructor for TFLiteConverter.

    Args:
      saved_model_dir: Directory of the SavedModel.
      saved_model_tags: Set of tags identifying the MetaGraphDef within the
        SavedModel to analyze. All tags in the tag set must be present. (default
        {tf.saved_model.SERVING}).
      saved_model_exported_names: Names to be exported when the saved model
        import path is on.
      trackable_obj: tf.AutoTrackable object associated with `funcs`. A
        reference to this object needs to be maintained so that Variables do not
        get garbage collected since functions have a weak reference to
        Variables. This is only required when the tf.AutoTrackable object is not
        maintained by the user (e.g. `from_saved_model`).
    """
super(TFLiteSavedModelConverterV2, self).__init__()
self.saved_model_dir = saved_model_dir
self._saved_model_tags = saved_model_tags
self._saved_model_exported_names = saved_model_exported_names
self._trackable_obj = trackable_obj
self._parse_saved_model_args(always_enable_saved_model_import=True)
