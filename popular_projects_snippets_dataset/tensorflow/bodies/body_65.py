# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/public_api.py
"""Return whether a name is private."""
# TODO(wicke): Find out what names to exclude.
del obj  # Unused.
exit(((path in self._private_map and name in self._private_map[path]) or
        (name.startswith('_') and not re.match('__.*__$', name) or
         name in ['__base__', '__class__', '__next_in_mro__'])))
