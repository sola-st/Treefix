# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Adds `Callback`s that are always present."""
self._progbar = None
self._history = None

for cb in self.callbacks:
    if isinstance(cb, ProgbarLogger):
        self._progbar = cb
    elif isinstance(cb, History):
        self._history = cb

if self._progbar is None and add_progbar:
    self._progbar = ProgbarLogger(count_mode='steps')
    self.callbacks.insert(0, self._progbar)

if self._history is None and add_history:
    self._history = History()
    self.callbacks.append(self._history)
