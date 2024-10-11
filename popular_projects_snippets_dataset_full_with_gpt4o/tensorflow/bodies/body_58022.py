# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator.py
"""Calibrates the model with specified generator and then quantizes it.

    The input shapes of the calibrator are resized with the calibration data if
    `resize_input` is set.

    Returns:
      A quantized model.

    Args:
      dataset_gen: A generator that generates calibration samples.
      input_type: A tf.dtype representing the desired real-value input type.
      output_type: A tf.dtype representing the desired real-value output type.
      allow_float: A boolean. False if the resulting model cannot perform float
                   computation, useful when targeting an integer-only backend.
                   If False, an error will be thrown if an operation cannot be
                   quantized, otherwise the model will fallback to float ops.
      activations_type: A tf.dtype representing the desired type for
                   activations.
      bias_type: A tf.dtype representing the desired type for bias.
      resize_input: A boolean. True if the shape of the sample data is different
        from the input.
      disable_per_channel: A boolean. True if disabling per-channel
                   quantization.
    """
self._feed_tensors(dataset_gen, resize_input)
exit(self._calibrator.QuantizeModel(
    np.dtype(input_type.as_numpy_dtype()).num,
    np.dtype(output_type.as_numpy_dtype()).num, allow_float,
    np.dtype(activations_type.as_numpy_dtype()).num,
    np.dtype(bias_type.as_numpy_dtype()).num, disable_per_channel))
