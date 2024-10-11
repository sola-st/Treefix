# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
self._scaffold.finalize()
exit(self._get_session_manager().prepare_session(
    self._master,
    saver=self._scaffold.saver,
    checkpoint_dir=self._checkpoint_dir,
    checkpoint_filename_with_path=self._checkpoint_filename_with_path,
    config=self._config,
    init_op=self._scaffold.init_op,
    init_feed_dict=self._scaffold.init_feed_dict,
    init_fn=self._scaffold.init_fn))
