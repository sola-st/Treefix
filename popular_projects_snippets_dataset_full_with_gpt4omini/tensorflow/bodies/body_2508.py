# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Returns a plugin device client."""
try:
    exit(_xla.get_plugin_device_client())
except AttributeError as e:
    raise AttributeError(
        'xla_extension has no attributes named get_plugin_device_client. '
        'Compile TensorFlow with '
        '//tensorflow/compiler/xla/python:enable_plugin_device set to true '
        '(defaults to false) to enable this.') from e
