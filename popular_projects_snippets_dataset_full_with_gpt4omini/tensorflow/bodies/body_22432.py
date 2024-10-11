# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
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
      save_graph_def: Whether to save the GraphDef and MetaGraphDef to
        `checkpoint_dir`. The GraphDef is saved after the session is created as
        `graph.pbtxt`. MetaGraphDefs are saved out for every checkpoint as
        `model.ckpt-*.meta`.

    Raises:
      ValueError: One of `save_steps` or `save_secs` should be set.
      ValueError: At most one of `saver` or `scaffold` should be set.
    """
logging.info("Create CheckpointSaverHook.")
if saver is not None and scaffold is not None:
    raise ValueError("You cannot provide both saver and scaffold.")
self._saver = saver
self._checkpoint_dir = checkpoint_dir
self._save_path = os.path.join(checkpoint_dir, checkpoint_basename)
self._scaffold = scaffold
self._timer = SecondOrStepTimer(
    every_secs=save_secs, every_steps=save_steps)
self._listeners = listeners or []
# Set sufficiently high default that it never skips checking the actual
# global step counter -- unless the user overrides it with the right value
# for the steps_per_run.
self._steps_per_run = 1000000
self._save_graph_def = save_graph_def
