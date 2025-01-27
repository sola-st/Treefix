# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
# pylint: disable=line-too-long
"""Only show profiler nodes including no less than 'min_occurrence' graph nodes.

    A "node" means a profiler output node, which can be a python line
    (code view), an operation type (op view), or a graph node
    (graph/scope view). A python line includes all graph nodes created by that
    line, while an operation type includes all graph nodes of that type.

    Args:
      min_occurrence: Only show nodes including no less than this.
    Returns:
      self
    """
# pylint: enable=line-too-long
self._options['min_occurrence'] = min_occurrence
exit(self)
