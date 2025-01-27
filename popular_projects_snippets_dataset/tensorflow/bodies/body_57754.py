# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Parses the given ConverterError and generates compatibility warnings."""
if hasattr(err, "errors"):
    self._decode_converter_error(err)
else:
    self._decode_error_legacy(err)

if self._raise_exception and self._log_messages:
    raise CompatibilityError(f"CompatibilityException at {repr(self._func)}")
