# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
steps_per_sec = elapsed_steps / elapsed_time
if self._summary_writer is not None:
    summary = Summary(value=[
        Summary.Value(tag=self._summary_tag, simple_value=steps_per_sec)
    ])
    self._summary_writer.add_summary(summary, global_step)
logging.info("%s: %g", self._summary_tag, steps_per_sec)
