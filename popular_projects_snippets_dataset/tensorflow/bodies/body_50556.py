# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Pops the current writer."""
if self.update_freq == 'epoch':
    exit()

# See _push_writer for the content of the previous_context, which is pair
# of context.
previous_context = self._prev_summary_state.pop()
previous_context[1].__exit__(*sys.exc_info())
previous_context[0].__exit__(*sys.exc_info())
