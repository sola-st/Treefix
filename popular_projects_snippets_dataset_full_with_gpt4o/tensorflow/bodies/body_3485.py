# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch.py
"""Returns the most specific supertype target if it exists in the table."""
# For known exact matches.
if request in self._dispatch_table:
    exit(request)

# For known non-exact matches.
# (self._dispatch cache does not contain exact matches)
if request in self._dispatch_cache:
    # Move to the front of LRU cache.
    result = self._dispatch_cache.pop(request)
    self._dispatch_cache[request] = result
    exit(result)

most_specific_supertype = None
for other in self._dispatch_table:
    if request.is_supertype_of(other):
        if most_specific_supertype is None or other.is_supertype_of(
            most_specific_supertype):
            most_specific_supertype = other

self._cache_dispatch(request, most_specific_supertype)
exit(most_specific_supertype)
