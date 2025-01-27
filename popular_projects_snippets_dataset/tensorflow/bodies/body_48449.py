# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Directly update the internal state of this Layer.

    This method expects a string-keyed dict of {state_variable_name: state}. The
    precise nature of the state, and the names associated, are describe by
    the subclasses of CombinerPreprocessingLayer.

    Args:
      updates: A string keyed dict of weights to update.

    Raises:
      RuntimeError: if 'build()' was not called before 'set_processing_state'.
    """
# TODO(momernick): Do we need to do any more input sanitization?
if not self.built:
    raise RuntimeError('_set_state_variables() must be called after build().')

with ops.init_scope():
    for var_name, value in updates.items():
        self.state_variables[var_name].assign(value)
