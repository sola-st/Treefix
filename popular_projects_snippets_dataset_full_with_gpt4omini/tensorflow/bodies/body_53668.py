# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/registry.py
"""Registers a Python object "candidate" for the given "name".

    Args:
      candidate: The candidate object to add to the registry.
      name: An optional string specifying the registry key for the candidate.
            If None, candidate.__name__ will be used.
    Raises:
      KeyError: If same name is used twice.
    """
if not name:
    name = candidate.__name__
if name in self._registry:
    frame = self._registry[name][_LOCATION_TAG]
    raise KeyError(
        "Registering two %s with name '%s'! "
        "(Previous registration was in %s %s:%d)" %
        (self._name, name, frame.name, frame.filename, frame.lineno))

logging.vlog(1, "Registering %s (%s) in %s.", name, candidate, self._name)
# stack trace is [this_function, Register(), user_function,...]
# so the user function is #2.
stack = traceback.extract_stack(limit=3)
stack_index = min(2, len(stack) - 1)
if stack_index >= 0:
    location_tag = stack[stack_index]
else:
    location_tag = ("UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN")
self._registry[name] = {_TYPE_TAG: candidate, _LOCATION_TAG: location_tag}
