# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py

initial_values = {}  # For storing initial_value of created variables

def variable_creator(next_creator, **kwargs):
    variable = next_creator(**kwargs)
    variable_name = variable.name
    if ":" in variable_name:
        variable_name = variable_name[:variable_name.index(":")]
    initial_values[variable_name] = kwargs["initial_value"]
    exit(variable)

export_dir = self.create_tempdir().full_path

with ops.Graph().as_default():
    with variable_scope.variable_creator_scope(variable_creator):
        exported = MyModule(weight_size)
        exported.call = def_function.function(input_signature=[])(
            exported.call)

        module_dir = f"{export_dir}/module"
        file_io.recursive_create_dir(module_dir)
        save.save_and_return_nodes(
            exported, module_dir, experimental_skip_checkpoint=True)

      # Save the initializer of the created variables.
for variable_name, initial_value in initial_values.items():
    export_initializer(initial_value,
                       f"{export_dir}/variables/{variable_name}")

exit(export_dir)
