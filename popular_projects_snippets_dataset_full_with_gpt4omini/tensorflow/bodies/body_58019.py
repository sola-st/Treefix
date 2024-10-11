# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator.py
"""Constructor.

    Args:
      model_content: Content of a TF-Lite Flatbuffer file.
      custom_op_registerers_by_name: List of str (symbol names) that take a
        pointer to a MutableOpResolver and register custom ops.
      custom_op_registerers_by_func: List of functions that take a pointer to a
        MutableOpResolver and register custom ops.

    Raises:
      ValueError: If the calibrator was unable to open the model.
    """
if not model_content:
    raise ValueError("`model_content` must be specified.")
if custom_op_registerers_by_name is None:
    custom_op_registerers_by_name = []
if custom_op_registerers_by_func is None:
    custom_op_registerers_by_func = []
try:
    self._calibrator = (
        _calibration_wrapper.CalibrationWrapper(
            model_content, custom_op_registerers_by_name,
            custom_op_registerers_by_func))
    self._model_content = model_content
except Exception as e:
    raise ValueError("Failed to parse the model: %s." % e)
if not self._calibrator:
    raise ValueError("Failed to parse the model.")
self._interpreter = None
