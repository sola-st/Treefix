# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Runs `fn(*args, **kwargs)` on `colocate_with` devices.

    Used to update non-slot variables.

    DEPRECATED: TF 1.x ONLY.

    Args:
      colocate_with: Devices returned by `non_slot_devices()`.
      fn: Function to execute.
      args: Tuple or list. Positional arguments to pass to `fn()`.
      kwargs: Dict with keyword arguments to pass to `fn()`.
      group: Boolean. Defaults to True. If False, the return value will be
        unwrapped.

    Returns:
      Return value of `fn`, possibly merged across devices.
    """
_require_cross_replica_or_default_context_extended(self)
if kwargs is None:
    kwargs = {}
fn = autograph.tf_convert(
    fn, autograph_ctx.control_status_ctx(), convert_by_default=False)
with self._container_strategy().scope():
    exit(self._update_non_slot(colocate_with, fn, args, kwargs, group))
