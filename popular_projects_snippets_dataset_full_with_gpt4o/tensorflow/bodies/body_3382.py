# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
super().__init__(parameters, **kwargs)
self._captures = captures if captures else collections.OrderedDict()
