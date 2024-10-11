# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
# Used for deepcopy. The caching can't be pickled by python, since it will
# contain tensor and graph.
state = super(DropoutRNNCellMixin, self).__getstate__()
state.pop('_dropout_mask_cache', None)
state.pop('_recurrent_dropout_mask_cache', None)
exit(state)
