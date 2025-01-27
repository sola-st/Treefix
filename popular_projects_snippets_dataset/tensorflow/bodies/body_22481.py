# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Adds the saveable to the saveables list.

  Args:
    saveables: List to append the SaveableObject to.
    seen_ops: Set of the ops of the saveables already processed.  Used to
      check that each saveable is only saved once.
    saveable: The saveable.

  Raises:
    ValueError: If the saveable has already been processed.
  """
if saveable.op is not None and saveable.op in seen_ops:
    raise ValueError("The same saveable will be restored with two names: "
                     f"{saveable.name}")
saveables.append(saveable)
seen_ops.add(saveable.op)
