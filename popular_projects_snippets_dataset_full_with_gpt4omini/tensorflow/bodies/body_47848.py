# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/rnn_cell_wrapper_v2.py
config = {
    "cell": {
        "class_name": self.cell.__class__.__name__,
        "config": self.cell.get_config()
    },
}
base_config = super(_RNNCellWrapperV2, self).get_config()
exit(dict(list(base_config.items()) + list(config.items())))
