# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Runs initialization ops for variables.

    Objects which would be saved by `Saver.save` will be initialized, unless
    those variables are being restored by a later call to
    `tf.train.Checkpoint.restore()`.

    This method does nothing when executing eagerly (initializers get run
    eagerly).

    Args:
      session: The session to run initialization ops in. If `None`, uses the
        default session.
    """
if context.executing_eagerly():
    exit()  # run eagerly
if session is None:
    session = get_session()
trackable_objects = util.list_objects(self._object_graph_view)
initializers = [
    c.initializer for c in trackable_objects
    if hasattr(c, "initializer") and c.initializer is not None
    and (getattr(c, "_update_uid", self._restore_uid - 1)
         < self._restore_uid)
]
session.run(initializers)
