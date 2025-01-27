# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint.py
"""Initializes a `CheckpointSaverHook`.

    Args:
      checkpoint_dir: `str`, base directory for the checkpoint files.
      save_secs: `int`, save every N secs.
      save_steps: `int`, save every N steps.
      saver: `Saver` object, used for saving.
      checkpoint_basename: `str`, base name for the checkpoint files.
      scaffold: `Scaffold`, use to get saver object.
      listeners: List of `CheckpointSaverListener` subclass instances. Used for
        callbacks that run immediately before or after this hook saves the
        checkpoint.

    Raises:
      ValueError: One of `save_steps` or `save_secs` should be set.
      ValueError: At most one of `saver` or `scaffold` should be set.
    """
save_path = os.path.join(checkpoint_dir, checkpoint_basename)
logging.info("Create AsyncCheckpointSaverHook saving to path\n%s",
             save_path)
if listeners:
    logging.info(" with %d listener(s).", len(listeners))
if saver is not None and scaffold is not None:
    raise ValueError("You cannot provide both saver and scaffold.")
self._saver = saver
self._save_thread = None
self._write_graph_thread = None
self._checkpoint_dir = checkpoint_dir
self._save_path = save_path
self._scaffold = scaffold
self._timer = basic_session_run_hooks.SecondOrStepTimer(
    every_secs=save_secs, every_steps=save_steps)
self._listeners = listeners or []
self._steps_per_run = 1
self._summary_writer = None
self._global_step_tensor = None

self._last_checkpoint_step = None

# Initialize the first timestamp for _END_TIME_OF_LAST_WRITE.
global _END_TIME_OF_LAST_WRITE
with _END_TIME_OF_LAST_WRITE_LOCK:
    if _END_TIME_OF_LAST_WRITE is None:
        _END_TIME_OF_LAST_WRITE = time.time()
