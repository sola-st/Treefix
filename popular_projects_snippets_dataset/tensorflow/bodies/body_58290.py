# Extracted from ./data/repos/tensorflow/tensorflow/cc/saved_model/testdata/generate_saved_models.py
self.x = variables.Variable(1.0, name="variable_x")
self.y = variables.Variable(2.0, name="variable_y")
self.child = module.Module()
self.child.z = variables.Variable(3.0, name="child_variable")
self.child.c = ops.convert_to_tensor(5.0)
