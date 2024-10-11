# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/async_checkpoint.py
global_step = run_context.session.run(self._global_step_tensor)
if self._timer.should_trigger_for_step(global_step):
    self._timer.update_last_triggered_step(global_step)
    logging.info("Triggering checkpoint. %s", global_step)
    if self._save(run_context.session, global_step):
        run_context.request_stop()
