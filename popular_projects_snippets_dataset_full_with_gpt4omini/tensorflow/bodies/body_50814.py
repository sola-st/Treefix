# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
"""Registers a candidate object under the package, name and predicate."""
if not isinstance(package, str) or not isinstance(name, str):
    raise TypeError(
        f"The package and name registered to a {self.name} must be strings, "
        f"got: package={type(package)}, name={type(name)}")
if not callable(predicate):
    raise TypeError(
        f"The predicate registered to a {self.name} must be callable, "
        f"got: {type(predicate)}")
registered_name = package + "." + name
if not _VALID_REGISTERED_NAME.match(registered_name):
    raise ValueError(
        f"Invalid registered {self.name}. Please check that the package and "
        f"name follow the regex '{_VALID_REGISTERED_NAME.pattern}': "
        f"(package='{package}', name='{name}')")
if registered_name in self._registered_map:
    raise ValueError(
        f"The name '{registered_name}' has already been registered to a "
        f"{self.name}. Found: {self._registered_map[registered_name]}")

self._registered_map[registered_name] = candidate
self._registered_predicates[registered_name] = predicate
self._registered_names.append(registered_name)
