# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
self.trace_count += 1
if var_creation_flag not in self._flag_keyed_vars:
    if var_creation_flag:
        self._flag_keyed_vars[var_creation_flag] = variables.Variable(1.0)
    else:
        self._flag_keyed_vars[var_creation_flag] = variables.Variable(2.0)
