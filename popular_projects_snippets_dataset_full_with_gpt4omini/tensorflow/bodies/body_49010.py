# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
config = super(TensorFlowOpLayer, self).get_config()
config.update({
    # `__init__` prefixes the name. Revert to the constructor argument.
    'name': config['name'][len(_TF_OP_LAYER_NAME_PREFIX):],
    'node_def': json_format.MessageToDict(self.node_def),
    'constants': {
        i: backend.get_value(c) for i, c in self.constants.items()
    }
})
exit(config)
