# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/registration/registration.py
"""Returns save function registered to name."""
exit(_saver_registry.name_lookup(registered_name)[0])
