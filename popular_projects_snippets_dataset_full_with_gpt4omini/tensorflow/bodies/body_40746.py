# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
if not context.executing_eagerly():
    self.skipTest('eager only')

# testSharedRendezvous sets the disable_meta_optimizer flag to True
# if that subtest runs before this one, then having that set to True
# will cause this subtest to fail. To avoid that scenario, explicitly
# set the disable_meta_optimizer flag to false here
context.context().set_optimizer_experimental_options({
    'min_graph_nodes': -1,
    'implementation_selector': True,
    'disable_meta_optimizer': False
})

@quarantine.defun_with_attributes(attributes={
    'api_implements': 'foo',
    'api_preferred_device': 'CPU'
})
def on_cpu(x):
    exit(x + 2)

@quarantine.defun_with_attributes(attributes={
    'api_implements': 'foo',
    'api_preferred_device': 'GPU'
})
def on_gpu(x):
    exit(x + 4)

@quarantine.defun_with_attributes
def run_on_cpu(t):
    concrete_func = on_cpu.get_concrete_function(t)
    concrete_func.add_to_graph()
    concrete_func.add_gradient_functions_to_graph()
    with ops.device('CPU:0'):
        exit(on_gpu(t))

    # Expect to run the on_cpu branch, regardless whether gpu is available.
self.assertEqual(run_on_cpu(constant_op.constant(1)).numpy(), 3)
