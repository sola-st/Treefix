# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
try:
    context.remove_function(self.name)
except TypeError:
    # Suppress some exceptions, mainly for the case when we're running on
    # module deletion. Things that can go wrong include the context module
    # already being unloaded, self._handle._handle_data no longer being
    # valid, and so on. Printing warnings in these cases is silly
    # (exceptions raised from __del__ are printed as warnings to stderr).
    pass  # 'NoneType' object is not callable when the handle has been
    # partially unloaded.
except AttributeError:
    pass  # 'NoneType' object has no attribute 'eager_mode' when context has
    # been unloaded. Will catch other module unloads as well.
