# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
options = config.get_optimizer_experimental_options()
self.assertIsNone(options.get('pin_to_host_optimization'))

@def_function.function
def fun():
    op = test_ops.device_placement_op()
    exit(op)

# Force optimizer to run for all graphs
config.set_optimizer_experimental_options({'min_graph_nodes': -1})
options['min_graph_nodes'] = -1

# Since pin to host is disabled, the operation should go on GPU
gpu = self.evaluate(fun())
self.assertIn(compat.as_bytes('GPU'), gpu)

config.set_optimizer_experimental_options(
    {'pin_to_host_optimization': True})
options['pin_to_host_optimization'] = True
self.assertDictEqual(config.get_optimizer_experimental_options(), options)
self.assertDictEqual(context.context().get_optimizer_experimental_options(),
                     options)

# Since pin to host is enabled, the operation should go on CPU
cpu = self.evaluate(fun())
self.assertIn(compat.as_bytes('CPU'), cpu)

config.set_optimizer_experimental_options(
    {'pin_to_host_optimization': False})
options['pin_to_host_optimization'] = False
self.assertDictEqual(config.get_optimizer_experimental_options(), options)
self.assertDictEqual(context.context().get_optimizer_experimental_options(),
                     options)

# Since pin to host is disabled again, the operation should go on GPU
gpu2 = self.evaluate(fun())
self.assertIn(compat.as_bytes('GPU'), gpu2)
