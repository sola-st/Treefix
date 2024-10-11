# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
# 1. Create a context with both CPU:0 and CPU:1.
context._reset_context()
cpus = context.context().list_physical_devices("CPU")
if len(cpus) == 1:
    context.context().set_logical_device_configuration(
        cpus[0], [
            context.LogicalDeviceConfiguration(),
            context.LogicalDeviceConfiguration()
        ])
context.ensure_initialized()

# 2. Create and save a model under a mirrored strategy.
file_name = os.path.join(self.get_temp_dir(), "saved_model.pb")
strategy = mirrored_strategy.MirroredStrategy(["CPU:0", "CPU:1"])
strategy.extended._use_var_policy = policy
with strategy.scope():
    root = autotrackable.AutoTrackable()
    root.v = variables.Variable([1., 1.], name="v")

    @def_function.function(input_signature=[])
    def f():
        root.v.assign([2., 2.])

    root.f = f

    save.export_meta_graph(
        obj=root,
        filename=file_name,
        options=save_options.SaveOptions(
            experimental_variable_policy=expand_strategy))

# 3. Read the output file and test behavior.
meta_graph_def = meta_graph.read_meta_graph_file(file_name)
object_graph = meta_graph_def.object_graph_def
graph_def = meta_graph_def.graph_def
v = next((n.variable
          for n in object_graph.nodes
          if n.HasField("variable") and n.variable.name == "v"), None)
saved_function = next((f for f in graph_def.library.function
                       if "inference_f_" in f.signature.name), None)
self.assertIsNotNone(saved_function)
if (expand_strategy ==
    save_options.VariablePolicy.EXPAND_DISTRIBUTED_VARIABLES):
    # experimental_save_variable_devices should have been automatically set.
    self.assertIn("CPU:0", v.device)
    components = v.experimental_distributed_variable_components
    self.assertLen(components, 2)
    v0 = next((x for x in components if x.name == "v"), None)
    v1 = next((x for x in components if x.name == "v/replica_1"), None)
    self.assertIsNotNone(v0)
    self.assertIsNotNone(v1)
    self.assertIn("CPU:0", v0.device)
    self.assertIn("CPU:1", v1.device)
    self.assertLen(saved_function.signature.input_arg, 2)
else:
    self.assertEmpty(v.device)
    self.assertEmpty(v.experimental_distributed_variable_components)
    self.assertLen(saved_function.signature.input_arg, 1)
