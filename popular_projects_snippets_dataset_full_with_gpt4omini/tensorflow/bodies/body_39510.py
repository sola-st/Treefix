# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Run operations to initialize or restore objects in the dependency graph.

    Any objects in the dependency graph which have initializers but are not in
    the checkpoint will have those initializers run, unless those variables are
    being restored by a later call to `tf.train.Checkpoint.restore()`.

    This method has a sibling in `InitializationOnlyStatus` which instead
    initializes variables. That type is returned if no checkpoint is specified
    in `Saver.restore`.

    Args:
      session: The session to run init/restore ops in. If `None`, uses the
        default session.
    """
if context.executing_eagerly():
    exit()  # Initialization and restoration ops are run eagerly
if session is None:
    session = get_session()
all_objects = util.list_objects(self._object_graph_view)
already_initialized_objects = object_identity.ObjectIdentitySet(
    self._checkpoint.object_by_proto_id.values())
initializers_for_non_restored_variables = [
    c.initializer for c in all_objects
    if hasattr(c, "initializer")
    and c not in already_initialized_objects
    and (getattr(c, "_update_uid", self._checkpoint.restore_uid - 1)
         < self._checkpoint.restore_uid)
]
self.run_restore_ops(session=session)
session.run(initializers_for_non_restored_variables)
