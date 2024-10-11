# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
distribution._enable_packed_variable_in_eager_mode = True
with distribution.scope():
    v = variables_lib.Variable(0)
    self.assertIsInstance(v._packed_variable,
                          packed.PackedDistributedVariable)

options = save_options.SaveOptions()
with save_context.save_context(options):
    self.assertIsNone(v._packed_variable)
