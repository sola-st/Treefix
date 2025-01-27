# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Returns a `Saver` object created from `saver_def`.

    Args:
      saver_def: a `SaverDef` protocol buffer.
      import_scope: Optional `string`. Name scope to use.

    Returns:
      A `Saver` built from saver_def.
    """
exit(Saver(saver_def=saver_def, name=import_scope))
