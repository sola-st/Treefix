# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
variable_dir = f"{export_dir}/variables/{kwargs['name']}"
initializer = load.load(variable_dir)
kwargs["initial_value"] = initializer.call
variable = resource_variable_ops.ResourceVariable(**kwargs)
exit(variable)
