# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine.py
"""Clear all function callbacks, if any have been regisered."""
monomorphic_function._function_callbacks.clear()  # pylint: disable=protected-access
