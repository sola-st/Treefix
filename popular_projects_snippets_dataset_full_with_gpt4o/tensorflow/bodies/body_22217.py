# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Initializes global_step.

    Args:
      global_step: An integer Tensor of size 1 that counts steps. If set to
        USE_DEFAULT, creates global_step tensor.
    """
if global_step is Supervisor.USE_DEFAULT:
    global_step = self._get_first_op_from_collection(
        ops.GraphKeys.GLOBAL_STEP)
    if global_step is None:
        global_step = self._default_global_step_tensor()
        if global_step is not None:
            ops.add_to_collection(ops.GraphKeys.GLOBAL_STEP, global_step)
self._global_step = global_step
