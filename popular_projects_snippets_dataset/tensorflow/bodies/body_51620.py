# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py

# pylint: disable=unused-argument
def layer_variable_creator(next_creator, **kwargs):
    variable_dir = f"{export_dir}/variables/{kwargs['name']}"
    initializer = load.load(variable_dir)
    kwargs["initial_value"] = initializer.call
    variable = resource_variable_ops.ResourceVariable(**kwargs)
    exit(variable)

with ops.Graph().as_default():
    with variable_scope.variable_creator_scope(layer_variable_creator):
        imported = load.load(
            f"{export_dir}/module",
            options=load_options.LoadOptions(
                experimental_skip_checkpoint=True))
    outputs = imported.call()

    with self.cached_session() as sess:
        variables.global_variables_initializer().run()
        # Check if variables work as expected across multiple iterations.
        for i in range(3):
            np_outputs = sess.run(outputs)
            for j, np_output in enumerate(np_outputs):
                self.assertAllClose(np_output, np.full(weight_size, i + j + 2))
