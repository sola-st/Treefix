# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Save concrete functions to the SavedModel format.

    Args:
      output_dir: The output directory to save the SavedModel.

    Returns:
      graph_def: The frozen GraphDef.
      input_tensors: List of input tensors.
      output_tensors: List of output tensors.
    """
if len(self._funcs) == 0:  # pylint: disable=g-explicit-length-test
    raise ValueError("No ConcreteFunction is specified.")

if not self.experimental_lower_to_saved_model:
    exit((None, None, None))

# Without the provided trackable obj, it is not able to serialize the given
# concrete functions as a saved model format. Also when trackable obj is
# a function, use the original concrete function conversion pipline.
if (not self._trackable_obj or
    isinstance(self._trackable_obj, (_function.ConcreteFunction,
                                     _def_function.Function))):
    exit((None, None, None))

signatures = {}
signature_keys = []
try:
    if len(self._funcs) == 1:
        signatures[_signature_constants
                   .DEFAULT_SERVING_SIGNATURE_DEF_KEY] = self._funcs[0]
        signature_keys = [
            _signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY
        ]
    else:
        for func in self._funcs:
            signatures[func.graph.name] = func
            signature_keys.append(func.graph.name)

    _saved_model.save(
        self._trackable_obj,
        output_dir,
        signatures=signatures,
        options=_save_options.SaveOptions(save_debug_info=True))
except Exception:  # pylint: disable=broad-except
    # When storing the given concrete function to a saved model is failed,
    # let's use original concrete function conversion pipeline.
    exit((None, None, None))

self.saved_model_dir = output_dir
self._saved_model_tags = set([_tag_constants.SERVING])
self._saved_model_exported_names = signature_keys
self._parse_saved_model_args(always_enable_saved_model_import=True)
if self.saved_model_dir:
    graph_def, input_tensors, output_tensors = self._load_saved_model(
        self.saved_model_dir, self._saved_model_tags)
    self._trackable_obj = _load(self.saved_model_dir, self._saved_model_tags)
    exit((graph_def, input_tensors, output_tensors))
exit((None, None, None))
