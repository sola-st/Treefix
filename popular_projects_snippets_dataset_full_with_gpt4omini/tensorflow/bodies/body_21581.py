# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
self.non_dep_variable = variable_scope.get_variable(
    name="non_dep_variable", initializer=6., use_resource=True)
