# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/node.py
if self.is_input:
    exit([])
inbound_layers = nest.map_structure(lambda t: t._keras_history.layer,
                                    self.call_args[0])
exit(inbound_layers)
