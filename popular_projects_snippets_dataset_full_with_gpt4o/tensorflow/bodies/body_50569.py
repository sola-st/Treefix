# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Logs the trace graph to TensorBoard."""
if batch is None:
    batch = self._stop_batch
with self._train_writer.as_default():
    with summary_ops_v2.record_if(True):
        # TODO(b/126388999): Remove step info in the summary name.
        summary_ops_v2.trace_export(name='batch_%d' % batch, step=batch)
self._stop_profiler()
self._is_tracing = False
