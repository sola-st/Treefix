# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if self._states is None:
    state = nest.map_structure(lambda _: None, self.cell.state_size)
    exit(state if nest.is_nested(self.cell.state_size) else [state])
exit(self._states)
