# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Only show profiler nodes holding no less than 'min_params' parameters.

    'Parameters' normally refers the weights of in TensorFlow variables.
    It reflects the 'capacity' of models.

    Args:
      min_params: Only show profiler nodes holding number parameters
          no less than this.
    Returns:
      self
    """
self._options['min_params'] = min_params
exit(self)
