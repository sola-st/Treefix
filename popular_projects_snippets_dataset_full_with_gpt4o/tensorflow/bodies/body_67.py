# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/public_api.py
"""Visitor interface, see `traverse` for details."""

# Avoid long waits in cases of pretty unambiguous failure.
if tf_inspect.ismodule(parent) and len(path.split('.')) > 10:
    raise RuntimeError('Modules nested too deep:\n%s.%s\n\nThis is likely a '
                       'problem with an accidental public import.' %
                       (self._root_name, path))

# Includes self._root_name
full_path = '.'.join([self._root_name, path]) if path else self._root_name

# Remove things that are not visible.
for name, child in list(children):
    if self._is_private(full_path, name, child):
        children.remove((name, child))

self._visitor(path, parent, children)

# Remove things that are visible, but which should not be descended into.
for name, child in list(children):
    if self._do_not_descend(full_path, name):
        children.remove((name, child))
