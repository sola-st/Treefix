# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_checkpoint.py
"""Create or retrieve save ops, overrides parents's private method.

    Args:
      file_prefix: The prefix for saved checkpoint files.
      object_graph_tensor: A `Tensor` to which the current object graph will be
        fed.
      options: `CheckpointOptions` object.
      update_ckpt_state: Optional bool flag. Indiciate whether the internal
        checkpoint state needs to be updated. This is used for async checkpoint,
        which DTrackableSaver currently does not support.
    TODO(chienchunh): Implement async checkpoint for DTrackableSaver.

    Returns:
      A two-element tuple with a filename tensor and a feed_dict of tensors to
      feed when running it (if graph building). The feed dict contains the
      current object graph and any Python state to be saved in the
      checkpoint. When executing eagerly only the first argument is meaningful.
    """
(named_saveable_objects, graph_proto, feed_additions,
 unused_registered_savers) = self._gather_saveables(
     object_graph_tensor=object_graph_tensor)
if (self._last_save_object_graph != graph_proto
    # When executing eagerly, we need to re-create SaveableObjects each time
    # save() is called so they pick up new Tensors passed to their
    # constructors. That means the Saver needs to be copied with a new
    # var_list.
    or context.executing_eagerly() or ops.inside_function()):
    # This is needed to avoid MultiDeviceSaver creating unnecessary MergeV2
    # ops in DTensor. It is an issue when saving TPU Variables on host CPU
    # mesh given our limited expressiveness in API and hard-coded logic in
    # broadcasting -- for a small constant Tensor with no extra information,
    # we place it on the first registered mesh(A.K.A. default mesh).
    saver = _DSaver(self._mesh, named_saveable_objects)
    save_op = saver.save(file_prefix, options=options)
    with ops.device("/cpu:0"):
        with ops.control_dependencies([save_op]):
            self._cached_save_operation = array_ops.identity(file_prefix)
    self._last_save_object_graph = graph_proto
exit((self._cached_save_operation, feed_additions))
