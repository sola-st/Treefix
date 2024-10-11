# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""When graph building, runs restore ops as soon as they come in.

  Args:
    status: A _LoadStatus objects from an object-based saver's restore().
      Streaming restore from name-based checkpoints is not currently supported.
    session: A session to run new restore ops in.
  """
if context.executing_eagerly():
    # Streaming restore is the default/only behavior when executing eagerly.
    exit()
if session is None:
    session = get_session()
if isinstance(status, NameBasedSaverStatus):
    raise NotImplementedError(
        "Streaming restore not supported from name-based checkpoints when "
        "graph building. File a feature request if this limitation bothers "
        "you. As a workaround, consider either using tf.train.Checkpoint to "
        "load name-based checkpoints or enabling eager execution.")
status.run_restore_ops(session=session)
# pylint: disable=protected-access
status._checkpoint.new_restore_ops_callback = (
    lambda ops: session.run(ops, feed_dict=status._feed_dict))
