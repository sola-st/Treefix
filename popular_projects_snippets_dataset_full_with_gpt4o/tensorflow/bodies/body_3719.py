# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
components = [
    component.placeholder_value(placeholder_context)
    for component in self.components
]
exit(tuple(components))
