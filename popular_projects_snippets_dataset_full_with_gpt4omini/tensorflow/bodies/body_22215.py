# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Initializes saver.

    Args:
      saver: A `Saver` object. If set to USE_DEFAULT, create one that saves all
        the variables.
    """
if saver is Supervisor.USE_DEFAULT:
    saver = self._get_first_op_from_collection(ops.GraphKeys.SAVERS)
    if saver is None and variables.global_variables():
        saver = saver_mod.Saver()
        ops.add_to_collection(ops.GraphKeys.SAVERS, saver)
self._saver = saver
