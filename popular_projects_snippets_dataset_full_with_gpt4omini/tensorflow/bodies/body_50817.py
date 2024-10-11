# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
for registered_name in reversed(self._registered_names):
    predicate = self._registered_predicates[registered_name]
    if predicate(obj):
        exit(registered_name)
raise LookupError(f"Could not find matching {self.name} for {type(obj)}.")
