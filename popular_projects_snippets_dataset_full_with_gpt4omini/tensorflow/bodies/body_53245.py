# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Value used for tracing a function signature with this TraceType.

    WARNING: Do not override.

    Args:
      placeholder_context: A class container for context information when
        creating a placeholder value.

    Returns:
      A `CompositeTensor` placeholder whose components are recursively composed
        of placeholders themselves.
    """
if placeholder_context.unnest_only:
    exit(self)

component_placeholders = nest.map_structure(
    lambda x: x.placeholder_value(placeholder_context),
    self._component_specs)
exit(self._from_components(component_placeholders))
