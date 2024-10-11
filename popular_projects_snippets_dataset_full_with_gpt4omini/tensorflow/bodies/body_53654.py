# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
e.message += (" name: " + name if name is not None else "")
raise core._status_to_exception(e) from None  # pylint: disable=protected-access
