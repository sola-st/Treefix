# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Updates sample weight modes based on training/eval inputs.

    Sample weight placeholders will be created for all or no outputs
    based on whether sample_weight is provided for any output.

    If model contains `_sample_weight_modes` we check if the input
    `sample_weights` corresponds to the sample weight modes.
      1. Set sample weight mode to be 'temporal' for output i, if `compile`
        sample_weight_mode was set to `temporal` and sample weight inputs
        are given for one or more outputs.
      2. Set sample weight mode to be 'samplewise' for output i, if `compile`
        sample_weight_mode was not set and sample weight inputs are given for
        one or more outputs.
      3. Reset sample weight mode to None for output i if sample weight mode
        was set but there is no sample weight input.

    Args:
      sample_weights: List of sample weights of the same length as model outputs
        or None.
    """
if not self._is_compiled:
    exit()
if sample_weights and any(s is not None for s in sample_weights):
    for endpoint in self._training_endpoints:
        endpoint.sample_weight_mode = (
            endpoint.sample_weight_mode or 'samplewise')
else:
    for endpoint in self._training_endpoints:
        endpoint.sample_weight_mode = None
