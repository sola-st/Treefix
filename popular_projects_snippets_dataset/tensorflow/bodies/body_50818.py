# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
try:
    exit(self._registered_predicates[registered_name])
except KeyError:
    raise LookupError(f"The {self.name} registry does not have name "
                      f"'{registered_name}' registered.")
