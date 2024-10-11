# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
try:
    exit(self._numpy_internal())
except core._NotOkStatusException as e:  # pylint: disable=protected-access
    raise core._status_to_exception(e) from None  # pylint: disable=protected-access
