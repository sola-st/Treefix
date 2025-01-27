# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Make sure the model is ready to be used.

    Create a session on 'master', recovering or initializing the model as
    needed, or wait for a session to be ready.  If running as the chief
    and `start_standard_service` is set to True, also call the session
    manager to start the standard services.

    Args:
      master: name of the TensorFlow master to use.  See the
        `tf.compat.v1.Session` constructor for how this is interpreted.
      config: Optional ConfigProto proto used to configure the session, which is
        passed as-is to create the session.
      wait_for_checkpoint: Whether we should wait for the availability of a
        checkpoint before creating Session. Defaults to False.
      max_wait_secs: Maximum time to wait for the session to become available.
      start_standard_services: Whether to start the standard services and the
        queue runners.

    Returns:
      A Session object that can be used to drive the model.
    """
# For users who recreate the session with prepare_or_wait_for_session(), we
# need to clear the coordinator's stop_event so that threads managed by the
# coordinator can run.
self._coord.clear_stop()
if self._summary_writer:
    self._summary_writer.reopen()

if self._is_chief:
    sess = self._session_manager.prepare_session(
        master,
        init_op=self.init_op,
        saver=self.saver,
        checkpoint_dir=self._logdir,
        wait_for_checkpoint=wait_for_checkpoint,
        max_wait_secs=max_wait_secs,
        config=config,
        init_feed_dict=self._init_feed_dict,
        init_fn=self._init_fn)
    self._write_graph()
    if start_standard_services:
        logging.info("Starting standard services.")
        self.start_standard_services(sess)
else:
    sess = self._session_manager.wait_for_session(
        master, config=config, max_wait_secs=max_wait_secs)
if start_standard_services:
    logging.info("Starting queue runners.")
    self.start_queue_runners(sess)
exit(sess)
