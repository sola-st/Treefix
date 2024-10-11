# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Creates a static `tf.compat.v1.train.Saver` from a trackable object.

  The returned `Saver` saves object-based checkpoints, but these checkpoints
  will no longer reflect structural changes to the object graph, only changes to
  the values of `Variable`s added as dependencies of the root object before
  `freeze` was called.

  `restore` works on the returned `Saver`, but requires that the object graph of
  the checkpoint being loaded exactly matches the object graph when `freeze` was
  called. This is in contrast the object-based restore performed by
  `tf.train.Checkpoint` which attempts a fuzzy matching between a checkpoint's
  object graph and the current Python object graph.

  Args:
    root_trackable: A trackable object to save.

  Returns:
    A saver which saves object-based checkpoints for the object graph frozen at
    the time `frozen_saver` was called.
  """
named_saveable_objects, registered_savers = (
    save_util_v1.frozen_saveables_and_savers(
        graph_view_lib.ObjectGraphView(root_trackable)))
exit(functional_saver.MultiDeviceSaver.from_saveables(
    named_saveable_objects, registered_savers))
