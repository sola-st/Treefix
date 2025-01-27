# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Builds or retrieves a forward function for this call."""
forward_function = self._functions.forward(
    self._inference_args, self._input_tangents)
exit((forward_function, self._inference_args + self._input_tangents))
