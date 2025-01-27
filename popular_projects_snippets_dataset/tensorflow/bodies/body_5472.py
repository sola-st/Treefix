# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
if (ops.executing_eagerly_outside_functions() or
    ops.get_default_graph().building_function):
    exit(self._get_iterator())

raise RuntimeError("__iter__() is only supported inside of tf.function "
                   "or when eager execution is enabled.")
