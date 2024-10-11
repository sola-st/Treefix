# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Create or retrieve save ops.

    Args:
      file_prefix: The prefix for saved checkpoint files.
      object_graph_tensor: A `Tensor` to which the current object graph will be
        fed.
      options: `CheckpointOptions` object.

    Returns:
      A two-element tuple with a filename tensor and a feed_dict of tensors to
      feed when running it (if graph building). The feed dict contains the
      current object graph and any Python state to be saved in the
      checkpoint. When executing eagerly only the first argument is meaningful.
    """
serialized_tensors, feed_additions, registered_savers, graph_proto = (
    self._gather_serialized_tensors(object_graph_tensor))

if (self._last_save_object_graph != graph_proto
    # When executing eagerly, we need to re-create SaveableObjects each
    # time save() is called so they pick up new Tensors passed to their
    # constructors. That means the Saver needs to be copied with a new
    # var_list.
    or context.executing_eagerly() or ops.inside_function()):
    saver = functional_saver.MultiDeviceSaver(serialized_tensors,
                                              registered_savers)
    save_op = saver.save(file_prefix, options=options)
    with ops.device("/cpu:0"):
        with ops.control_dependencies([save_op]):
            self._cached_save_operation = array_ops.identity(file_prefix)
    self._last_save_object_graph = graph_proto
exit((self._cached_save_operation, feed_additions))
