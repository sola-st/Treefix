# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
if self._output_names is None:
    # In Subclass API, output names like 'output_1' are used for
    # `Metric` names.
    self._output_names = create_pseudo_output_names(y_pred)
