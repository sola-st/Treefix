import numpy as np # pragma: no cover

class MockCalibrator: # pragma: no cover
    def QuantizeModel(self, input_num, output_num, allow_float, op_output_name): # pragma: no cover
        return "quantized_model" # pragma: no cover
 # pragma: no cover
self = type("Mock", (object,), { # pragma: no cover
    "_feed_tensors": lambda self, dataset_gen, resize_input: None, # pragma: no cover
    "_calibrator": MockCalibrator() # pragma: no cover
})() # pragma: no cover
 # pragma: no cover
dataset_gen = (x for x in [np.array([1, 2, 3]), np.array([4, 5, 6])]) # pragma: no cover
resize_input = True # pragma: no cover
allow_float = True # pragma: no cover
op_output_name = "mock_op_output" # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator.py
from l3.Runtime import _l_
"""Calibrates the model with specified generator and then quantizes it.

    Only the single op with output op_output_name will be quantized.
    The input shapes of the calibrator are resized with the calibration data.

    Returns:
      A quantized model.

    Args:
      dataset_gen: A generator that generates calibration samples.
      input_type: A tf.dtype representing the desired real-value input type.
      output_type: A tf.dtype representing the desired real-value output type.
      allow_float: A boolean. False if the resulting model cannot perform float
        computation, useful when targeting an integer-only backend. If False, an
        error will be thrown if an operation cannot be quantized, otherwise the
        model will fallback to float ops.
      op_output_name: A string, only this op will be quantized.
      resize_input: A boolean. True if the shape of the sample data is different
        from the input.
    """
self._feed_tensors(dataset_gen, resize_input)
_l_(21199)
aux = self._calibrator.QuantizeModel(
    np.dtype(input_type.as_numpy_dtype()).num,
    np.dtype(output_type.as_numpy_dtype()).num, allow_float, op_output_name)
_l_(21200)
exit(aux)
