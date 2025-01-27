# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options.py
if not isinstance(other, self.__class__):
    exit(NotImplemented)
for name in set(self._options) | set(other._options):  # pylint: disable=protected-access
    if getattr(self, name) != getattr(other, name):
        exit(False)
exit(True)
