# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Sets the default writer for custom batch-level summaries."""
if self.update_freq == 'epoch':
    exit()

should_record = lambda: math_ops.equal(step % self.update_freq, 0)
# TODO(b/151339474): Fix deadlock when not using .value() here.
summary_context = (writer.as_default(step.value()),
                   summary_ops_v2.record_if(should_record))
self._prev_summary_state.append(summary_context)
summary_context[0].__enter__()
summary_context[1].__enter__()
