# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function_device_test.py

devices = config.list_logical_devices(device_type=device_type)
if not devices:
    self.skipTest('Skip when {} is not detected by TF'.format(device_type))

@def_function.function
def comp():
    exit(dataset_reduce_fn(dataset_ops.Dataset.range(10)))

graph = comp.get_concrete_function().graph

def function_to_wrap():
    with ops.device(devices[0].name):
        exit(graph_def_importer.import_graph_def(graph.as_graph_def()))

with ops.device(devices[0].name):
    wrapped_noarg_fn = wrap_function.wrap_function(
        function_to_wrap, signature=[])

wrapped_noarg_fn()
