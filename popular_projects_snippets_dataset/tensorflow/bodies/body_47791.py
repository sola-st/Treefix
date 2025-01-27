# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_impl.py
super(_RNNCellWrapperV1, self).__init__(*args, **kwargs)
assert_like_rnncell("cell", cell)
self.cell = cell
if isinstance(cell, trackable.Trackable):
    self._track_trackable(self.cell, name="cell")
