# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
self._registry_name = name
# Maps registered name -> object
self._registered_map = {}
# Maps registered name -> predicate
self._registered_predicates = {}
# Stores names in the order of registration
self._registered_names = []
