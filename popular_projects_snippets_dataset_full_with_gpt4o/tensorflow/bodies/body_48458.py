# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_preprocessing_layer.py
"""Disallow calling a method inside a `tf.function`."""
if ops.inside_function():
    error_msg = (
        'Detected a call to `PreprocessingLayer.{method_name}` inside a '
        '`tf.function`. `PreprocessingLayer.{method_name} is a high-level '
        'endpoint that manages its own `tf.function`. Please move the call '
        'to `PreprocessingLayer.{method_name}` outside of all enclosing '
        '`tf.function`s. Note that you can call a `PreprocessingLayer` '
        'directly on `Tensor`s inside a `tf.function` like: `layer(x)`, '
        'or update its state like: `layer.update_state(x)`.').format(
            method_name=method_name)
    raise RuntimeError(error_msg)
