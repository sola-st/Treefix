# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Custom pickling, to omit unpickleable objects."""
result = self.__dict__.copy()
del result["_lock"]
del result["_descriptor_cache"]
del result["_key_for_call_stats"]
exit(result)
