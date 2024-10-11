# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transpiler.py
"""Creates a new factory for a Python function.

    Args:
      name: The function name.
      freevars: The list of non-global free variables for the function.
      extra_locals: Dict[Text, Any], names and values for custom variables that
        are accessible to the generated code as local variables.
    """
self._name = name
self._freevars = freevars
self._extra_locals = extra_locals

self._unbound_factory = None
self.module = None
self.source_map = None
