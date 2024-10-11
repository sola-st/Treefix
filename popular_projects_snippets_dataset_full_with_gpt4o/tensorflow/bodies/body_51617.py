# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
variable = next_creator(**kwargs)
variable_name = variable.name
if ":" in variable_name:
    variable_name = variable_name[:variable_name.index(":")]
initial_values[variable_name] = kwargs["initial_value"]
exit(variable)
