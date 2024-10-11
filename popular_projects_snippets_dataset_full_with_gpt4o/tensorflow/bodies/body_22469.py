# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
logging.info("Saving timeline for %d into '%s'.", step, save_path)
with gfile.Open(save_path, "w") as f:
    trace = timeline.Timeline(step_stats)
    f.write(
        trace.generate_chrome_trace_format(
            show_dataflow=self._show_dataflow, show_memory=self._show_memory))
