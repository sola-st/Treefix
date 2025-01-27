# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
if isinstance(cell, DropoutRNNCellMixin):
    cell.reset_dropout_mask()
    cell.reset_recurrent_dropout_mask()
