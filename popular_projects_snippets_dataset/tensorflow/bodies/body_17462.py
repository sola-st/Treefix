# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""For implementing `Trackable`."""
new_variable = None
if options.experimental_variable_policy._save_variable_devices():  # pylint:disable=protected-access
    with ops.device(self.device):
        new_variable = copy_to_graph_uninitialized(self)
else:
    new_variable = copy_to_graph_uninitialized(self)
object_map[self] = new_variable
tensor_map[self.handle] = new_variable.handle
exit([self.handle])
