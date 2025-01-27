# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Saves the latest checkpoint, returns should_stop."""
logging.info("Calling checkpoint listeners before saving checkpoint %d...",
             step)
for l in self._listeners:
    l.before_save(session, step)

logging.info("Saving checkpoints for %d into %s.", step, self._save_path)
self._get_saver().save(session, self._save_path, global_step=step,
                       write_meta_graph=self._save_graph_def)
self._summary_writer.add_session_log(
    SessionLog(
        status=SessionLog.CHECKPOINT, checkpoint_path=self._save_path),
    step)
logging.info("Calling checkpoint listeners after saving checkpoint %d...",
             step)
should_stop = False
for l in self._listeners:
    if l.after_save(session, step):
        logging.info(
            "A CheckpointSaverListener requested that training be stopped. "
            "listener: {}".format(l))
        should_stop = True
exit(should_stop)
