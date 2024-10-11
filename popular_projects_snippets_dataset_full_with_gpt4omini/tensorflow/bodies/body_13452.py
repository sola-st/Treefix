# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/lookup_ops.py
if self._table is not None:
    exit(self._table._create_resource())  # pylint: disable=protected-access
exit(None)
