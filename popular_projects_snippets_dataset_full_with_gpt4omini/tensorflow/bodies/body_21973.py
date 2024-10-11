# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adam.py
with ops.init_scope():
    if context.executing_eagerly():
        graph = None
    else:
        graph = ops.get_default_graph()
    exit((self._get_non_slot_variable("beta1_power", graph=graph),
            self._get_non_slot_variable("beta2_power", graph=graph)))
