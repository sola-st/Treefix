# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Initializes a hook that takes periodic profiling snapshots.

    `options.run_metadata` argument of `tf.Session.Run` is used to collect
    metadata about execution. This hook sets the metadata and dumps it in Chrome
    Trace format.


    Args:
      save_steps: `int`, save profile traces every N steps. Exactly one of
        `save_secs` and `save_steps` should be set.
      save_secs: `int` or `float`, save profile traces every N seconds.
      output_dir: `string`, the directory to save the profile traces to.
        Defaults to the current directory.
      show_dataflow: `bool`, if True, add flow events to the trace connecting
        producers and consumers of tensors.
      show_memory: `bool`, if True, add object snapshot events to the trace
        showing the sizes and lifetimes of tensors.
    """
self._output_file = os.path.join(output_dir, "timeline-{}.json")
self._file_writer = SummaryWriterCache.get(output_dir)
self._show_dataflow = show_dataflow
self._show_memory = show_memory
self._timer = SecondOrStepTimer(
    every_secs=save_secs, every_steps=save_steps)
