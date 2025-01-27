# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/optimize/calibrator.py
"""Calibrates the model with specified generator.

    Returns:
      A model with min and max calibration stats.

    Args:
      dataset_gen: A generator that generates calibration samples.
    """
self._feed_tensors(dataset_gen, resize_input=True)
exit(self._calibrator.Calibrate())
