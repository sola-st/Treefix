# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/utils_v1/export_output.py
"""Constructor for PredictOutput.

    Args:
      outputs: A `Tensor` or a dict of string to `Tensor` representing the
        predictions.

    Raises:
      ValueError: if the outputs is not dict, or any of its keys are not
          strings, or any of its values are not `Tensor`s.
    """

self._outputs = self._wrap_and_check_outputs(
    outputs, self._SINGLE_OUTPUT_DEFAULT_NAME, error_label='Prediction')
