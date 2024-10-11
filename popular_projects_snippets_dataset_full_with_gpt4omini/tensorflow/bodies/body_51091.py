# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
context._reset_context()
cpus = context.context().list_physical_devices("CPU")
if len(cpus) == 1:
    context.context().set_logical_device_configuration(
        cpus[0], [
            context.LogicalDeviceConfiguration(),
            context.LogicalDeviceConfiguration()
        ])
context.ensure_initialized()

root = autotrackable.AutoTrackable()
with ops.device("CPU:0"):
    root.v0 = variables.Variable(1., name="v0")
with ops.device("CPU:1"):
    root.v1 = variables.Variable(1., name="v1")

options = save_options.SaveOptions(
    experimental_variable_policy=save_devices)
file_name = os.path.join(self.get_temp_dir(), "saved_model")
if meta_graph_only:
    save.export_meta_graph(obj=root, filename=file_name, options=options)
else:
    save.save(obj=root, export_dir=file_name, options=options)

meta = None
if meta_graph_only:
    meta = meta_graph.read_meta_graph_file(file_name)
else:
    meta = loader_impl.parse_saved_model(file_name).meta_graphs[0]

# Check devices in meta graph nodes.
graph_def = meta.graph_def
v0 = next((n for n in graph_def.node if n.name == "v0"), None)
v1 = next((n for n in graph_def.node if n.name == "v1"), None)
self.assertIsNotNone(v0)
self.assertIsNotNone(v1)
if save_devices == save_options.VariablePolicy.SAVE_VARIABLE_DEVICES:
    self.assertIn("CPU:0", v0.device)
    self.assertIn("CPU:1", v1.device)
else:
    self.assertEmpty(v0.device)
    self.assertEmpty(v1.device)

# Check devices in object graph nodes.
object_graph_def = meta.object_graph_def
v0 = next((n.variable
           for n in object_graph_def.nodes
           if n.HasField("variable") and n.variable.name == "v0"), None)
v1 = next((n.variable
           for n in object_graph_def.nodes
           if n.HasField("variable") and n.variable.name == "v1"), None)
self.assertIsNotNone(v0)
self.assertIsNotNone(v1)
if save_devices == save_options.VariablePolicy.SAVE_VARIABLE_DEVICES:
    self.assertIn("CPU:0", v0.device)
    self.assertIn("CPU:1", v1.device)
else:
    self.assertEmpty(v0.device)
    self.assertEmpty(v1.device)
