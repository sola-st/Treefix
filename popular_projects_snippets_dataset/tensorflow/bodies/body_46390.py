# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
"""Create a new scope.

    Args:
      parent: A Scope or None.
      isolated: Whether the scope is isolated, that is, whether variables
        modified in this scope should be considered modified in the parent
        scope.
      function_name: Name of the function owning this scope.
    """
self.parent = parent
self.isolated = isolated
self.function_name = function_name

self.isolated_names = set()

self.read = set()
self.modified = set()
self.deleted = set()

self.bound = set()
self.globals = set()
self.nonlocals = set()
self.annotations = set()

self.params = weakref.WeakValueDictionary()

# Certain fields can only be accessed after the scope and all its parent
# scopes have been fully built. This field guards that.
self.is_final = False
