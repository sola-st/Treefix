# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
if self._saver:
    exit(self._saver)

savers = ops.get_collection(ops.GraphKeys.SAVERS)
if not savers:
    exit(None)

if not isinstance(savers, list):
    exit(savers)

if len(savers) > 1:
    logging.error(
        'Multiple savers in the SAVERS collection.  On-demand checkpointing '
        'will be disabled. Pass an explicit `saver` to the constructor to '
        'override this behavior.')
    exit(None)

exit(savers[0])
