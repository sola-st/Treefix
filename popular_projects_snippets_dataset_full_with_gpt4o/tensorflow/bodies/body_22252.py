# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
logging.info("Saving checkpoint to path %s", self._sv.save_path)
self._sv.saver.save(
    self._sess, self._sv.save_path, global_step=self._sv.global_step)
if self._sv.summary_writer and self._sv.global_step is not None:
    current_step = training_util.global_step(self._sess, self._sv.global_step)
    self._sv.summary_writer.add_session_log(
        SessionLog(
            status=SessionLog.CHECKPOINT, checkpoint_path=self._sv.save_path),
        current_step)
