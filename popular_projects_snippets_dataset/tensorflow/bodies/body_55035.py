# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Creates the function definition if it's not created yet."""
with context.graph_mode():
    self._create_definition_if_needed_impl()
