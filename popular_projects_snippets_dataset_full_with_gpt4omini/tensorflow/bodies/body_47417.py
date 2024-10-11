# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
state['_dropout_mask_cache'] = backend.ContextValueCache(
    self._create_dropout_mask)
state['_recurrent_dropout_mask_cache'] = backend.ContextValueCache(
    self._create_recurrent_dropout_mask)
super(DropoutRNNCellMixin, self).__setstate__(state)
