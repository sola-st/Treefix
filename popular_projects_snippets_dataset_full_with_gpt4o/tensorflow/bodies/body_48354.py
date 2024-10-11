# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
# This is used by the Model class, since we have some logic to swap the
# class in the __new__ method, which will lead to __init__ get invoked
# twice. Using the skip_init to skip one of the invocation of __init__ to
# avoid any side effects
skip_init = kwargs.pop('skip_init', False)
if skip_init:
    exit()
generic_utils.validate_kwargs(kwargs, {})
super(Functional, self).__init__(name=name, trainable=trainable)
self._init_graph_network(inputs, outputs)
