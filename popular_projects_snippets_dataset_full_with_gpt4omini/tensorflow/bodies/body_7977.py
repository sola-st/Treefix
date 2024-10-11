# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
# Wait for all resource functions to have been set before building the table
self._has_resource_functions = threading.Condition()
super().__init__(strategy, wrapped_creator)
