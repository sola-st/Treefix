# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""For implementing `Trackable`."""
if save_type == "checkpoint":
    exit({})
exit({f"trace_{n}": fn for n, fn in
        enumerate(self._list_all_concrete_functions_for_serialization())})
