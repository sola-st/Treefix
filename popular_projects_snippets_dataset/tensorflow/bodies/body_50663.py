# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/fake_summary_writer.py
if (global_step is not None) and (global_step < 0):
    raise ValueError('Invalid global_step %s.' % global_step)
self._added_run_metadata[tag] = run_metadata
