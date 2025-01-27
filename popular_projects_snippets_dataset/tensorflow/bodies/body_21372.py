# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
# pylint: disable=line-too-long
"""Saves variables.

    This method runs the ops added by the constructor for saving variables.
    It requires a session in which the graph was launched.  The variables to
    save must also have been initialized.

    The method returns the path prefix of the newly created checkpoint files.
    This string can be passed directly to a call to `restore()`.

    Args:
      sess: A Session to use to save the variables.
      save_path: String.  Prefix of filenames created for the checkpoint.
      global_step: If provided the global step number is appended to `save_path`
        to create the checkpoint filenames. The optional argument can be a
        `Tensor`, a `Tensor` name or an integer.
      latest_filename: Optional name for the protocol buffer file that will
        contains the list of most recent checkpoints.  That file, kept in the
        same directory as the checkpoint files, is automatically managed by the
        saver to keep track of recent checkpoints.  Defaults to 'checkpoint'.
      meta_graph_suffix: Suffix for `MetaGraphDef` file. Defaults to 'meta'.
      write_meta_graph: `Boolean` indicating whether or not to write the meta
        graph file.
      write_state: `Boolean` indicating whether or not to write the
        `CheckpointStateProto`.
      strip_default_attrs: Boolean. If `True`, default-valued attributes will be
        removed from the NodeDefs. For a detailed guide, see [Stripping
        Default-Valued
        Attributes](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/saved_model/README.md#stripping-default-valued-attributes).
      save_debug_info: If `True`, save the GraphDebugInfo to a separate file,
        which in the same directory of save_path and with `_debug` added before
        the file extension. This is only enabled when `write_meta_graph` is
        `True`

    Returns:
      A string: path prefix used for the checkpoint files.  If the saver is
        sharded, this string ends with: '-?????-of-nnnnn' where 'nnnnn'
        is the number of shards created.
      If the saver is empty, returns None.

    Raises:
      TypeError: If `sess` is not a `Session`.
      ValueError: If `latest_filename` contains path components, or if it
        collides with `save_path`.
      RuntimeError: If save and restore ops weren't built.
    """
# pylint: enable=line-too-long
start_time = time.time()
if not self._is_built and not context.executing_eagerly():
    raise RuntimeError(
        "`build()` should be called before save if defer_build==True")
if latest_filename is None:
    latest_filename = "checkpoint"
if self._write_version != saver_pb2.SaverDef.V2:
    logging.warning("*******************************************************")
    logging.warning("TensorFlow's V1 checkpoint format has been deprecated.")
    logging.warning("Consider switching to the more efficient V2 format:")
    logging.warning("   `tf.train.Saver(write_version=tf.train.SaverDef.V2)`")
    logging.warning("now on by default.")
    logging.warning("*******************************************************")

if os.path.split(latest_filename)[0]:
    raise ValueError("'latest_filename' must not contain path components")

save_path = compat.as_str(save_path)
if global_step is not None:
    if not isinstance(global_step, compat.integral_types):
        global_step = training_util.global_step(sess, global_step)
    checkpoint_file = "%s-%d" % (save_path, global_step)
    if self._pad_step_number:
        # Zero-pads the step numbers, so that they are sorted when listed.
        checkpoint_file = "%s-%s" % (save_path, "{:08d}".format(global_step))
else:
    checkpoint_file = save_path
    if os.path.basename(save_path) == latest_filename and not self._sharded:
        # Guard against collision between data file and checkpoint state file.
        raise ValueError(
            "'latest_filename' collides with 'save_path': '%s' and '%s'" %
            (latest_filename, save_path))

if (not context.executing_eagerly() and
    not isinstance(sess, session.SessionInterface)):
    raise TypeError("'sess' must be a Session; %s" % sess)

save_path_parent = os.path.dirname(save_path)
if not self._is_empty:
    try:
        if context.executing_eagerly():
            self._build_eager(
                checkpoint_file, build_save=True, build_restore=False)
            model_checkpoint_path = self.saver_def.save_tensor_name
        else:
            model_checkpoint_path = sess.run(
                self.saver_def.save_tensor_name,
                {self.saver_def.filename_tensor_name: checkpoint_file})

        model_checkpoint_path = compat.as_str(model_checkpoint_path)
        if write_state:
            self._RecordLastCheckpoint(model_checkpoint_path)
            checkpoint_management.update_checkpoint_state_internal(
                save_dir=save_path_parent,
                model_checkpoint_path=model_checkpoint_path,
                all_model_checkpoint_paths=self.last_checkpoints,
                latest_filename=latest_filename,
                save_relative_paths=self._save_relative_paths)
            self._MaybeDeleteOldCheckpoints(meta_graph_suffix=meta_graph_suffix)
    except (errors.FailedPreconditionError, errors.NotFoundError) as exc:
        if not gfile.IsDirectory(save_path_parent):
            exc = ValueError(
                "Parent directory of {} doesn't exist, can't save.".format(
                    save_path))
        raise exc

end_time = time.time()
metrics.AddCheckpointWriteDuration(
    api_label=_SAVER_LABEL,
    microseconds=_get_duration_microseconds(start_time, end_time))
global _END_TIME_OF_LAST_WRITE
with _END_TIME_OF_LAST_WRITE_LOCK:
    metrics.AddTrainingTimeSaved(
        api_label=_SAVER_LABEL,
        microseconds=_get_duration_microseconds(_END_TIME_OF_LAST_WRITE,
                                                end_time))
    _END_TIME_OF_LAST_WRITE = end_time

if write_meta_graph:
    meta_graph_filename = checkpoint_management.meta_graph_filename(
        checkpoint_file, meta_graph_suffix=meta_graph_suffix)
    if not context.executing_eagerly():
        with sess.graph.as_default():
            self.export_meta_graph(
                meta_graph_filename,
                strip_default_attrs=strip_default_attrs,
                save_debug_info=save_debug_info)

if self._is_empty:
    exit(None)
else:
    metrics.RecordCheckpointSize(
        api_label=_SAVER_LABEL,
        filesize=_get_checkpoint_size(model_checkpoint_path))
    exit(model_checkpoint_path)
