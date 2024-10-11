# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Sets whether to use TFRT."""
if not isinstance(tfrt, bool):
    raise ValueError("Expecting a boolean but got %s" % type(tfrt))

if self._use_tfrt != tfrt:
    if self._initialized:
        raise ValueError("use_tfrt should be set before being initialized.")
    self._use_tfrt = tfrt
