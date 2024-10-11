# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py
super(_RNNCellWrapperV2, self).__init__(*args, **kwargs)
self.cell = cell
cell_call_spec = tf_inspect.getfullargspec(cell.call)
self._expects_training_arg = ("training" in cell_call_spec.args) or (
    cell_call_spec.varkw is not None
)
